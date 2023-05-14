import typer
from database_context import Context

_context = Context()
app = typer.Typer()

subjects_lst = {
    "LRM": "LINEAR_REGRESSION_MODELS",
    "DOE": "DESIGN_OF_EXPERIMENTS",
}


@app.command("commands")
def commands():
    command_lst = {
        "subjects": "Show list of subjects. ARGUMENTS: None",
        "create_session / create": "To create a new session. ARGUMENTS: subject, segment_no",
        "end_session": "To end a session. ARGUMENTS: session_id",
        "show_progress": "To show overall progress. ARGUMENTS: ",
        "show_progress_for": "To show progress for certain subject. ARGUMENTS: subject",
        "calcualate_score_for": "To calculate total score for a subject. ARGUMENTS: subject",
        "add_score_status": "Change or add score for a progress record. ARGUMENTS: subject, segment_no",
    }
    for key, value in command_lst.items():
        print(key, ":    ", value)


@app.command("subjects")
def subjects():
    for key, value in subjects_lst.items():
        print(key, ":   ", value)


@app.command("create_session")
@app.command("create")
def create(subject, segment_no):
    query = f"set @session_id = 0;CALL spCreateSession('{subject}',{segment_no},@session_id);select @session_id;"
    session_id = _context.run_sql_get_data(query)[0]
    print(f"You are now studying {subject}'s {segment_no}. Your session_id is {session_id}")


@app.command("end_session")
def EndSession(session_id):
    """
    End a session
    @param session_id: id of the active session
    @return: None
    """
    _context.run_sql(f"UPDATE SESSION SET EndDate = now() where Id = {session_id};")
    """WRITE TO EXCEL SHEET"""
    print("Session ended successfully.")


@app.command("show_progress")
def ShowProgress():
    """
    Show all the progress records
    @return: list: progress data
    """
    for progress in _context.run_procedure("spShowProgress", []):
        print(progress)


@app.command("show_progress_for")
def ShowProgressFor(subject, segment_no):
    """
    Show progress for certain subject and segment #
    @param subject: str: subject key
    @param segment_no: int: segment_no
    @return:
    """
    for progress in _context.run_procedure("spShowProgressFor", [subjects_lst[subject.upper()], segment_no]):
        print(progress)


@app.command("calculate_score_for")
def CalculateScoreFor(subject):
    """
    Calculate percentage of score for certain subject
    @param subject: str: Name of the subject
    @return: int: percentage
    """
    if subject == "--":
        subject = ""
    else:
        subject = subjects_lst[subject.upper()]
    data = _context.run_procedure("spGetQuizScore", [subject])
    if len(data) < 1:
        print("Nothing to show.")
        return
    print(str(calculate(data)) + "%")


@app.command("add_score_status")
def AddScoreStatus(subject):
    pass


def calculate(data):
    if len(data) < 1:
        return 0

    marks = 0
    out_of_marks = 0
    for d in data:
        s = list(d)[0].split('/')
        marks += float(s[0])
        out_of_marks += float(s[1])

    return (marks / out_of_marks) * 100
