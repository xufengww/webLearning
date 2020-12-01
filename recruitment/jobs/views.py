from django.shortcuts import render
from jobs.models import Job
from django.template import loader
from jobs.models import Cities, JobTypes
from django.http import HttpResponse, Http404


# Create your views here.

def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}

    for job in job_list:
        job.job_city = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]

    return HttpResponse(template.render(context))


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.job_city = Cities[job.job_city][1]

        return render(request, 'job.html', context={'job': job})
    except Job.DoesNotExit:
        raise Http404("Job does not exist")




