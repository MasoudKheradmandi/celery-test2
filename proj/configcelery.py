broker_url = 'redis://localhost:6379'
result_backend = 'mongodb://localhost:27017'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

timezone = 'Asia/Tehran'
enable_utc = True

include = ['proj.tasks']