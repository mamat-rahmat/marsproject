from django.urls import path, include
from django.conf.urls.static import static
from alcproject import settings
from .forms import UserProfileRegistrationForm
from .views import (
    index,
    # ProgramListView,
    program_list,
    # MyProgramListView,
    my_program_list,
    # SpecialProgramListView,
    special_program_list,
    # ProgramDetailView,
    program_detail,
    program_register,
    exam_detail,
    UserProfileRegistrationView,
    edit_profile,
    topic_list,
    topic_detail,
    topic_create,
)


urlpatterns = [
    path('accounts/register/', UserProfileRegistrationView.as_view(), name='registration_register'),
    path('accounts/edit', edit_profile, name='edit-profile'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', index, name='index'),
    path('program', program_list, name='program-list'),
    path('myprogram', my_program_list, name='my-program-list'),
    path('sprogram', special_program_list, name='special-program-list'),
    path('program/<int:pk>', program_detail, name='program-detail'),
    path('program/<int:pk>/register', program_register, name='program-register'),
    path('program/<int:pk_program>/exam/<int:pk_exam>', exam_detail, name='exam-detail'),
    path('program/<int:pk_program>/topic', topic_list, name='topic-list'),
    path('program/<int:pk_program>/topic/<int:pk_topic>', topic_detail, name='topic-detail'),
    path('program/<int:pk_program>/topic/create', topic_create, name='topic-create'),
]
