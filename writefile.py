import time as t
import xlwings as xl


def writeExcel(job_names, job_hrefs, job_types):
    """
    写excel
    :param job_names:
    :param job_hrefs:
    :param job_types:
    :return:
    """
    app = xl.App()

    wb = app.books.active
    ws = wb.sheets.active

    ws.name = "岗位明细"
    ws.range("A1").value = "在招岗位"
    ws.range("B1").value = "JD链接"
    ws.range("C1").value = "职位类别"

    ws.range("A2").options(transpose=True).value = job_names
    ws.range("B2").options(transpose=True).value = job_hrefs
    ws.range("C2").options(transpose=True).value = job_types
    wb.save(r"./抓取{0}.xlsx".format(t.strftime("%Y%m%d%H%M%S", t.localtime())))
