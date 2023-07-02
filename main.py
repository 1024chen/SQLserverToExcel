from excel import excel_operator as excel
from excel import file_operator as file
from db import db


def start_trans() -> bool:
    excel.res_output(
        excel.data_to_excel(
            db.query_data(), file.path()
        )
    )


if __name__ == '__main__':
    start_trans()
