from core.models import Program, UserProfile, BIDANG_CHOICES, Membership
from django.contrib.auth.models import User


program = dict()
for bidang, _ in BIDANG_CHOICES:
    program[bidang] = Program.objects.get(bidang=bidang,
                                          name__endswith='Gelombang 1')

for userprofile in UserProfile.objects.all():
    print(userprofile, '---', program[userprofile.bidang])
    membership, created = Membership.objects.get_or_create(user=userprofile.user,
                                                           program=program[userprofile.bidang])
    membership.paid = True
    membership.save()
