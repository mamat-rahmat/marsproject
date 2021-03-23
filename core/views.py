from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.forms.models import model_to_dict
from .models import Program, Exam, Membership, Answer, UserProfile, Topic, Post
from .forms import AnswerForm, UserProfileRegistrationForm, UserProfileForm, TopicForm, PostForm
from registration.backends.simple.views import RegistrationView


def index(request):
    context = {
        'siswa_count' : UserProfile.objects.filter(role="SISWA").count(),
        'guru_count' : UserProfile.objects.filter(role="GURU").count(),
        'sekolah_count' : UserProfile.objects.values('sekolah').distinct().count(),
        'program_count' : Program.objects.all().count(),
    }
    return render(request, 'core/index.html', context)


def program_list(request):
    programs = Program.objects.filter(special_program=False).order_by('-id')
    for program in programs:
        if request.user.is_anonymous:
            memberships = []
        else:
            memberships = Membership.objects.filter(user=request.user,
                                                    program=program,
                                                    paid=True)
        program.is_registered = bool(memberships)
    context = {'programs': programs}
    return render(request, 'core/program_list.html', context)


@login_required
def my_program_list(request):
    memberships = Membership.objects.filter(user=request.user, paid=True)
    programs = Program.objects.filter(membership__in=memberships).order_by('-id')
    for program in programs:
        program.is_registered = True
    context = {'programs': programs}
    return render(request, 'core/my_program_list.html', context)


def special_program_list(request):
    programs = Program.objects.filter(special_program=True).order_by('-id')
    for program in programs:
        if request.user.is_anonymous:
            memberships = []
        else:
            memberships = Membership.objects.filter(user=request.user,
                                                    program=program,
                                                    paid=True)
        program.is_registered = bool(memberships)
    context = {'programs': programs}
    return render(request, 'core/special_program_list.html', context)


def program_detail(request, pk):
    program = Program.objects.get(pk=pk)
    memberships = Membership.objects.filter(user=request.user,
                                            program=program)
    if not memberships:
        program.status = 'unregistered'
    elif memberships[0].paid:
        program.status = 'registered'
    else:
        program.status = 'pending'

    context = {'program': program}
    return render(request, 'core/program_detail.html', context)


@login_required
def program_register(request, pk):
    program = Program.objects.get(pk=pk)
    membership, created = Membership.objects.get_or_create(user=request.user,
                                                           program=program,
                                                           paid=True)
    return redirect('program-detail', pk=pk)


@login_required
def exam_detail(request, pk_program, pk_exam):
    program = get_object_or_404(Program, pk=pk_program)
    exam = get_object_or_404(Exam, pk=pk_exam)
    membership_set = request.user.membership_set.filter(user=request.user,
                                                        program=program,
                                                        paid=True)

    if not membership_set:
        return HttpResponse('Unauthorized Access', status=401)
    if not exam.program.id == program.id:
        return HttpResponse('Unauthorized Access', status=401)

    saved = False
    myanswer, created = Answer.objects.get_or_create(user=request.user,
                                                     exam=exam)
    myanskey = exam.problemset
    if request.method == "POST":
        for i in range(1, 51):
            num = f"no{i:02}"
            setattr(myanswer, num, request.POST.get(f"no{i:02}", '-'))
        myanswer.save()
        myanswer.grade()
        saved = True

    ranking = []
    if exam.is_ended:
        answers = Answer.objects.select_related('user__userprofile').filter(exam=exam, user__userprofile__role='SISWA')
        members = Membership.objects.select_related('user__userprofile').filter(program=program, user__userprofile__role='SISWA')
        scores = dict()
        for member in members:
            scores[member.user] = 0
        for answer in answers:
            scores[answer.user] = answer.score
        for user, score in scores.items():
            userprofile = user.userprofile
            item = [
                userprofile.nama_lengkap,
                userprofile.sekolah,
                score
            ]
            ranking.append(item)
        ranking.sort(key=lambda x: x[-1], reverse=True)
        ranking = [[idx+1]+val for idx,val in enumerate(ranking)]

    context = {
        'program': program,
        'exam': exam,
        'answer': model_to_dict(myanswer),
        'anskey': model_to_dict(myanskey),
        'sidebar': True,
        'ranking': ranking,
        'saved': saved
    }
    return render(request, 'core/exam_detail.html', context)


class UserProfileRegistrationView(RegistrationView):

    form_class = UserProfileRegistrationForm
    success_url = 'program-list'

    def register(self, form_class):
        new_user = super(UserProfileRegistrationView, self).register(form_class)
        user_profile = UserProfile()
        user_profile.user = new_user
        user_profile.nama_lengkap = form_class.cleaned_data['nama_lengkap']
        user_profile.nomor_whatsapp = form_class.cleaned_data['nomor_whatsapp']
        user_profile.sekolah = form_class.cleaned_data['sekolah']
        user_profile.kota = form_class.cleaned_data['kota']
        user_profile.provinsi = form_class.cleaned_data['provinsi']
        user_profile.bidang = form_class.cleaned_data['bidang']
        user_profile.guru_pembimbing = form_class.cleaned_data['guru_pembimbing']
        user_profile.nomor_guru_pembimbing = form_class.cleaned_data['nomor_guru_pembimbing']
        user_profile.save()
        return new_user

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('edit-profile')
    form = UserProfileForm(instance=request.user.userprofile)
    context = {
        'form': form
    }
    return render(request, 'core/edit_profile.html', context)


@login_required
def topic_list(request, pk_program):
    program = get_object_or_404(Program, pk=pk_program)
    membership_set = request.user.membership_set.filter(user=request.user,
                                                        program=program,
                                                        paid=True)

    if not membership_set:
        return HttpResponse('Unauthorized Access', status=401)

    object_list = Topic.objects.filter(program=program)
    context = {
        'program': program,
        'object_list': object_list
    }
    return render(request, 'core/topic_list.html', context)


@login_required
def topic_detail(request, pk_program, pk_topic):
    program = get_object_or_404(Program, pk=pk_program)
    topic = get_object_or_404(Topic, pk=pk_topic)
    
    if not topic.program.id == program.id:
        return HttpResponse('Unauthorized Access', status=401)
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post()
            post.topic = topic
            post.author = request.user
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('topic-detail', pk_program=pk_program, pk_topic=topic.id)
    
    form = PostForm()
    context = {
        'program': program,
        'topic': topic,
        'form': form
    }
    return render(request, 'core/topic_detail.html', context)

@login_required
def topic_create(request, pk_program):
    program = get_object_or_404(Program, pk=pk_program)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = Topic()
            topic.program = program
            topic.author = request.user
            topic.title = form.cleaned_data['title']
            topic.content = form.cleaned_data['content']
            topic.save()
            return redirect('topic-list', pk_program=pk_program)
    
    form = TopicForm()
    context = {
        'form': form,
        'program': program
    }
    return render(request, 'core/topic_create.html', context)
