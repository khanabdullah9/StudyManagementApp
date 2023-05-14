from database_context import Context
from cli_commands import app

# ENTRY POINT
if __name__ == "__main__":
    # app()
    _context = Context()
    print(_context.create_param_str(['LINEAR_REGRESSION_MODELS',1]))
    # result = _context.run_procedure(proc_name="spShowProgressFor", proc_params=['LINEAR_REGRESSION_MODELS',1])
    # for r in result:
    #     print(r)
