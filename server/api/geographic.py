"""
SIMRP Geographic Module
Geographic data and postal code lookup.
"""
from core import execute


def get_geo_options(handler, body, client_ip):
    """Get kecamatan/kelurahan options."""
    rows = execute("""
        SELECT kecamatan.id AS kec_id, kecamatan.name AS kec_name, 
               kelurahan.id AS kel_id, kelurahan.name AS kel_name
        FROM kecamatan LEFT JOIN kelurahan ON kelurahan.kecamatan_id = kecamatan.id
        ORDER BY kecamatan.name, kelurahan.name
    """).fetchall()
    
    grouped = {}
    for r in rows:
        if r["kec_id"] not in grouped:
            grouped[r["kec_id"]] = {"id": r["kec_id"], "name": r["kec_name"], "kelurahan": []}
        if r["kel_id"]:
            grouped[r["kec_id"]]["kelurahan"].append({"id": r["kel_id"], "name": r["kel_name"]})
    
    return handler.send_json(200, {"kecamatan": list(grouped.values())})


def get_geo_stats(handler, body, client_ip):
    """Get geographic statistics."""
    kec_count = execute("SELECT COUNT(*) as c FROM kecamatan").fetchone()["c"]
    kel_count = execute("SELECT COUNT(*) as c FROM kelurahan").fetchone()["c"]
    postal_count = execute("SELECT COUNT(*) as c FROM postal_codes").fetchone()["c"]
    return handler.send_json(200, {"stats": {"kecamatan": kec_count, "kelurahan": kel_count, "kodepos": postal_count}})


def get_by_postal_code(handler, body, client_ip, code):
    """Get kelurahan by postal code."""
    rows = execute("""
        SELECT postal_codes.code AS kodepos, kelurahan.name AS kelurahan, kecamatan.name AS kecamatan
        FROM postal_codes
        JOIN kampung_mapping ON kampung_mapping.postal_code_id = postal_codes.id
        JOIN kelurahan ON kelurahan.id = kampung_mapping.kelurahan_id
        JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
        WHERE postal_codes.code = ? ORDER BY kelurahan.name
    """, (code,)).fetchall()
    
    if not rows:
        return handler.send_json(404, {"error": "Kodepos tidak ditemukan"})
    
    return handler.send_json(200, {"kodepos": code, "kelurahan": [dict(r) for r in rows]})


def get_kampung(handler, body, client_ip):
    """Get all kelurahan with XP."""
    user = handler.get_current_user()
    if not user:
        return handler.send_json(401, {"error": "Unauthorized"})
    
    rows = execute("""
        SELECT kelurahan.id, kelurahan.name AS name, kecamatan.name AS kecamatan, xp_kelurahan.total_xp AS xp
        FROM kelurahan
        JOIN kecamatan ON kecamatan.id = kelurahan.kecamatan_id
        JOIN xp_kelurahan ON xp_kelurahan.kelurahan_id = kelurahan.id
        ORDER BY xp DESC LIMIT 100
    """).fetchall()
    
    return handler.send_json(200, {"kampung": [{"id": r["id"], "name": r["name"], "kecamatan": r["kecamatan"], "xp": int(r["xp"])} for r in rows]})


geographic_routes = {
    "GET": {
        "/geo/options": get_geo_options,
        "/geo/stats": get_geo_stats,
        "/kodepos/{code}": get_by_postal_code,
        "/kampung": get_kampung,
    },
}
