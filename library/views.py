import os
import boto3
from django.http import HttpResponse, Http404
from botocore.exceptions import NoCredentialsError
from django.shortcuts import render

def search_results(request):
    query = request.GET.get('q')
    results = []

    if query:
        s3 = boto3.client('s3')
        bucket_name = 'libraryassignment2bucket'

        # List objects in the specified S3 bucket
        try:
            response = s3.list_objects_v2(Bucket=bucket_name)
            for obj in response.get('Contents', []):
                file_name = obj['Key']
                if file_name.endswith('.txt') and query.lower() in file_name.lower():
                    results.append(file_name)
        except NoCredentialsError:
            return HttpResponse("AWS credentials not found.", status=500)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

    return render(request, 'search.html', {'results': results, 'query': query})

def download_file(request, file_name):
    s3 = boto3.client('s3')
    bucket_name = 'libraryassignment2bucket'

    try:
        # Download the file from S3
        s3.download_file(bucket_name, file_name, f'/tmp/{file_name}')

        # Serve the file as an HTTP response
        with open(f'/tmp/{file_name}', 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response

    except NoCredentialsError:
        return HttpResponse("AWS credentials not found.", status=500)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=500)

    