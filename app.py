from flask import Flask, render_template, request, Response, stream_with_context
import json
from invite import GitHubInviter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_invites():
    data = request.json
    token = data.get('token')
    owner = data.get('owner')
    repo = data.get('repo')
    tbi_file = data.get('tbi_file')
    success_file = data.get('success_file')
    max_invites = int(data.get('max_invites', 60))
    delay = float(data.get('delay', 3))
    usernames_raw = data.get('usernames', '')
    usernames_list = usernames_raw.split('\n') if usernames_raw.strip() else None

    inviter = GitHubInviter(
        token=token if token else None,
        owner=owner if owner else None,
        repo=repo if repo else None,
        tbi_file=tbi_file if tbi_file else None,
        success_file=success_file if success_file else None
    )

    def generate():
        for log in inviter.run(max_invites=max_invites, usernames_list=usernames_list, delay=delay):
            yield f"data: {json.dumps({'message': log})}\n\n"

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
