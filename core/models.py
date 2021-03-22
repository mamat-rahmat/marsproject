# pylint: disable=no-member
from django.db import models
from django.utils import timezone
from django.forms.models import model_to_dict
from django.contrib.auth.models import User


BIDANG_CHOICES = (
    ('matematika', 'Matematika SMA'),
    ('fisika', 'Fisika SMA'),
    ('kimia', 'Kimia SMA'),
    ('biologi', 'Biologi SMA'),
    ('komputer', 'Komputer SMA'),
    ('ekonomi', 'Ekonomi SMA'),
    ('astronomi', 'Astronomi SMA'),
    ('geografi', 'Geografi SMA'),
    ('kebumian', 'Kebumian SMA'),
    ('matematika-smp', 'Matematika SMP'),
    ('ipa-smp', 'IPA SMP'),
    ('ips-smp', 'IPS SMP'),
    ('matematika-sd', 'Matematika SD'),
    ('ipa-sd', 'IPA SD'),
)

ROLE_CHOICES = (
    ('SISWA', 'Siswa'),
    ('GURU', 'Guru'),
)

class UserProfile(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='SISWA')
    nomor_whatsapp = models.CharField(max_length=100)
    sekolah = models.CharField(max_length=100)
    kota = models.CharField(max_length=100)
    provinsi = models.CharField(max_length=100)
    bidang = models.CharField(max_length=20, choices=BIDANG_CHOICES, default='matematika')
    guru_pembimbing = models.CharField(max_length=100)
    nomor_guru_pembimbing = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_lengkap


class Program(models.Model):
    name = models.CharField(max_length=100)
    bidang = models.CharField(max_length=20, choices=BIDANG_CHOICES, default='matematika')
    open_registration_time = models.DateTimeField(blank=True, null=True)
    close_registration_time = models.DateTimeField(blank=True, null=True)
    price = models.IntegerField()
    special_program = models.BooleanField(default=False)
    download_file = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def is_opened(self):
        return timezone.now() >= self.open_registration_time

    def is_closed(self):
        return timezone.now() >= self.close_registration_time

    def exam_count(self):
        return self.exam_set.count()


class SelectedProgram(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)


class Tutorship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.program} - {self.paid}'

ANSWER_CHOICES = (
    ('-', '-'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
)


class Problemset(models.Model):
    name = models.CharField(max_length=100)
    problem_file = models.FileField()
    solution_file = models.FileField()
    no01 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no02 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no03 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no04 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no05 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no06 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no07 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no08 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no09 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no10 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no11 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no12 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no13 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no14 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no15 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no16 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no17 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no18 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no19 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no20 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no21 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no22 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no23 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no24 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no25 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no26 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no27 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no28 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no29 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no30 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no31 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no32 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no33 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no34 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no35 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no36 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no37 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no38 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no39 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no40 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no41 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no42 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no43 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no44 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no45 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no46 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no47 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no48 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no49 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no50 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    add_essay = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    def mcq_total(self):
        total = 0
        anskey = model_to_dict(self)
        for i in range(1,51):
            num = f"no{i:02}"
            if (anskey[num] != '-'):
                total += 1
        return total

    def mcq_empty(self):
        return self.mcq_total == 0

    def essay_empty(self):
        return not self.add_essay


class Exam(models.Model):
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    problemset = models.ForeignKey(Problemset, on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    correct_score = models.IntegerField(default=1)
    wrong_score = models.IntegerField(default=0)
    blank_score = models.IntegerField(default=0)
    score_in_percentage = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.name} - {self.program}'

    def is_started(self):
        return timezone.now() >= self.start_time

    def is_ended(self):
        return timezone.now() >= self.end_time


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    graded = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    no01 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no02 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no03 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no04 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no05 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no06 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no07 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no08 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no09 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no10 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no11 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no12 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no13 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no14 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no15 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no16 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no17 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no18 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no19 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no20 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no21 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no22 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no23 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no24 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no25 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no26 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no27 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no28 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no29 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no30 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no31 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no32 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no33 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no34 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no35 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no36 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no37 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no38 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no39 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no40 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no41 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no42 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no43 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no44 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no45 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no46 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no47 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no48 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no49 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')
    no50 = models.CharField(max_length=1, choices=ANSWER_CHOICES, default='-')

    class Meta:
        unique_together = (('user', 'exam'),)

    def __str__(self):
        answer = model_to_dict(self)
        choices = ''.join([answer[f'no{i:02}'] for i in range(1,51)])
        return f"{self.user} - {self.exam} - {self.score} - {choices}"

    def grade(self):
        problemset = self.exam.problemset
        exam = self.exam
        answer = model_to_dict(self)
        anskey = model_to_dict(problemset)
        total = problemset.mcq_total()

        correct_point = 0
        wrong_point = 0
        blank_point = 0
        for i in range(1,total+1):
            num = f"no{i:02}"
            if(answer[num] == '-'):
                blank_point += 1
            else:
                if (answer[num] == anskey[num]):
                    correct_point += 1
                else:
                    wrong_point += 1

        if total==0:
            self.score = 0
        else:
            if exam.score_in_percentage:
                self.score = int(100*correct_point/total)
            else:
                self.score = correct_point*exam.correct_score + \
                             wrong_point*exam.wrong_score + \
                             blank_point*exam.blank_score
        self.graded = True
        self.save()


class Topic(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
