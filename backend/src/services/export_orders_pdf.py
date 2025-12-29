import io
from fastapi import Response
from fastapi.responses import StreamingResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from src.order.schemas import GetOrder
from reportlab.pdfgen import canvas

def export_orders_pdf(orders):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    y = 800
    c.drawString(50, y, "Orders")
    y -= 30

    for o in orders:
        c.drawString(
            50, y,
            f"{o.id} | {o.customer.name} | {o.gas_volume} | {o.cost}"
        )
        y -= 20
        if y < 50:
            c.showPage()
            y = 800

    c.save()
    buf.seek(0)

    return Response(
        content=buf.getvalue(),
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=orders.pdf"
        }
    )
