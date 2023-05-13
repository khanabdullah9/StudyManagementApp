import typer
from database_context import Context

_context = Context()
app = typer.Typer()

@app.command("show_command_list")
@app.command("--h")
def show_command_list():
    command_lst = [
        "create_session        To create a new session. ARGUMENTS: subject, segment_no",
        "end_session           To end a session. ARGUMENTS: session_id",
        "show_progress         To show overall progress. ARGUMENTS: ",
        "calcualate_score_for  To calculate total score for a subject. ARGUMENTS: subject"
        "calcualate_score      To calculate total score for all subjects. ARGUMENTS: "
        ]
    for _ in command_lst:
        print(_)
	
@app.command("create_session")
@app.command("create")
def create(subject):
    query = f"set @session_id = 0;CALL spCreateSession({subject},1,@session_id);select @session_id;"
    session_id = _context.run_sql_get_data(query)[0]
    print(f"You are now studying {subject}'s {segment_no}. Your session_id is {session_id}")
    
    
@app.command("show_all_subjects")
def get_all_subjects():
    query = "select Name from subject;"
    names = _context.run_sql_get_data(query)
    for name in names:
        print(name)




