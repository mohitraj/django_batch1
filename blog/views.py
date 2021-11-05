from django.shortcuts import render, redirect
from .form import PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

