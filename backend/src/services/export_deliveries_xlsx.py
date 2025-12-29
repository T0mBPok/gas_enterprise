import io
from fastapi import Response
from openpyxl import Workbook
from src.delivery.schemas import GetDelivery


def export_deliveries_xlsx(deliveries: list[GetDelivery]):
    wb = Workbook()
    ws = wb.active

    ws.append([
        "ID",
        "Дата доставки",
        "Объем",
        "Предприятие",
        "Заказ",
        "Статус",
        "Транспорт",
    ])

    for d in deliveries:
        ws.append([
            d.id,
            d.delivery_date.strftime("%Y-%m-%d"),
            d.volume,
            d.enterprise.name,
            d.order.id,
            d.status.name,
            d.transport.name,
        ])

    buf = io.BytesIO()
    wb.save(buf)
    buf.seek(0)

    return Response(
        content=buf.getvalue(),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=deliveries.xlsx"
        }
    )