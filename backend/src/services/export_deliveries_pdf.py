import io
from fastapi import Response
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def export_deliveries_pdf(deliveries):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)

    y = 800
    c.drawString(50, y, "Deliveries")
    y -= 30

    for d in deliveries:
        c.drawString(
            50, y,
            f"{d.id} | {d.delivery_date} | {d.volume} | "
            f"{d.enterprise.name} | {d.order.id} | {d.status.name}"
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
            "Content-Disposition": "attachment; filename=deliveries.pdf"
        }
    )