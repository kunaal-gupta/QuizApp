from django.db import models
from django.contrib.auth.models import User
from training.models import Training
from phonenumber_field.modelfields import PhoneNumberField


class Quiz(models.Model):
    training = models.ForeignKey(Training, related_name='Quiz', on_delete=models.CASCADE)
    Question_per_quiz = models.IntegerField(default=1, help_text='Number of questions for each training quiz')
    Instruction = models.TextField(null=False, default="No instructions for this quiz", help_text="Enter Quiz instructions for this training ")
    # TODO:Kunaal to change below fild to format Hours:Minutes
    Timer_per_quiz = models.IntegerField(default=60, help_text="Enter time in minutes")
    Total_access_duration = models.IntegerField(default=30, help_text="Enter duration in days")
    file = models.FileField(default="training_name.csv", unique=True, help_text='Upload only CSV file with a nanme training_name.csv. Eg PMP.csv')



    # class Meta:
    #     ordering = training.Program_Code

    def __str__(self):
        return self.training.Program_Code + ": " + str(self.Question_per_quiz) + \
               " ques | " + str(self.Timer_per_quiz) + " mins | " + str(self.Total_access_duration) + " access days"


class UserProfile(models.Model):
    User_Code = models.AutoField(auto_created=True, primary_key=True, unique=True)
    User_Identity = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Phone_Number = PhoneNumberField()
    Program_Code = models.ForeignKey(Training, related_name='UserProfile', on_delete=models.CASCADE)
    Number_of_Quiz = models.IntegerField(default=1, help_text="Enter number of quizzes to assign. Max num = 3")

    Quiz1 = models.BooleanField(null=False, default=False, verbose_name="Activate Quiz 1", help_text="Click it to enable the Quiz1")
    Quiz2 = models.BooleanField(null=False, default=False, verbose_name="Activate Quiz 2", help_text="Click it to enable the Quiz1")
    Quiz3 = models.BooleanField(null=False, default=False, verbose_name="Activate Quiz 3", help_text="Click it to enable the Quiz1")

    Quiz_1_Score = models.IntegerField(null=True, blank=True, default=0)
    Quiz_2_Score = models.IntegerField(null=True, blank=True, default=0)
    Quiz_3_Score = models.IntegerField(null=True, blank=True, default=0)

    Quiz1_response = models.TextField(blank=True, default='')
    Quiz2_response = models.TextField(blank=True, default='')
    Quiz3_response = models.TextField(blank=True, default='')

    def __str__(self):
        return "User " + str(self.User_Code)


class Question(models.Model):
    Ques_No = models.CharField(max_length=20, primary_key=True, unique=True, help_text='Enter name as "trainingName No" eg. PMP1, DASM2')
    training = models.ForeignKey(Training, related_name='Question', on_delete=models.CASCADE)
    Ques = models.CharField(max_length=1000, blank=False)
    Option_1 = models.CharField(max_length=500, blank=False)
    Option_2 = models.CharField(max_length=500, blank=False)
    Option_3 = models.CharField(max_length=500, blank=True)
    Option_4 = models.CharField(max_length=500, blank=True)
    Option_5 = models.CharField(max_length=500, blank=True)
    Option_6 = models.CharField(max_length=500, blank=True)

    Correct_Option = models.CharField(max_length=500, blank=False)
    Answer_Description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.Ques_No)

