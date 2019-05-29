import click
import subprocess
import os

@click.group()
def cli():
    pass

@click.command()
@click.argument('keyword')
def find(keyword):
    click.echo('find job: '+ keyword)
    findcmd=["list-jobs"]
    command = build_jenkins_cmd(cmd=findcmd)
    p = subprocess.Popen(command, 
                        env=env,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT)
    #stdout,stderr = p.communicate()
    for line in p.stdout.readlines():
        if line.find(keyword) != -1:
            print line,
    retval = p.wait()


@click.command()
@click.argument('job_name')
def build(job_name):
    click.echo('build '+job_name)
    findcmd=["build", job_name]
    command = build_jenkins_cmd(cmd=findcmd)
    p = subprocess.Popen(command, 
                        env=env,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT)
    #stdout,stderr = p.communicate()
    for line in p.stdout.readlines():
        print line,
    retval = p.wait()
    

def build_jenkins_cmd(cmd):
    command = ['java', '-jar', 'jenkins-cli.jar','-s',url]
    command.extend(cmd)
    return command

def get_env():
    if 'JENKINS_API_TOKEN' in os.environ:
        apikey = os.environ['JENKINS_API_TOKEN']
    else:
        apikey = "minhuc123xdfaf"
    if 'JENKINS_USER_ID' in os.environ:
        userid = os.environ['JENKINS_USER_ID']
    else:
        userid = 'minhuc'
    if 'JENKINS_URL' in os.environ:
        url = os.environ['JENKINS_URL']
    else:
        url = "http://localhost:8080/"
    
    env={"JENKINS_API_TOKEN": apikey, "JENKINS_USER_ID": userid}
    return env, url

cli.add_command(find)
cli.add_command(build)

env, url = get_env()

if __name__ == '__main__':
    cli()


