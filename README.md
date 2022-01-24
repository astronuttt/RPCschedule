# RPCschedule

[apscheduler](https://github.com/agronholm/apscheduler) is a great package for scheduling jobs and things like this. But the problem is you can't use it in web apps (gunicorn, etc..) because they create multiple instances of the app and they will run in parallel. This also creates multiple instances of apscheduler objects, one in each app. this causes the scheduler to run a job multiple times and problems like this.

this project helps you solve this problem by running an instance of apscheduler in a seperate process and connecting to it with RPC, in this case [RPyC](https://github.com/tomerfiliba-org/rpyc)
