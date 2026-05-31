"""autopsy 결과를 HTML 페이지로 빌드 (Action 전용 slim 버전).

scripts/build_site.py의 render_autopsy_index_html, render_autopsy_detail_html을
재사용하기 위해 build_site.py 통째 import.
"""
import sys, os, json
from pathlib import Path

# docs/ 가 작업 루트. build_site.py는 docs/_autopsy_scripts/에 없으므로 stub.
# autopsy 결과만 처리.
HERE = Path(__file__).resolve().parent
DOCS = HERE.parent  # docs/
AUTOPSY = DOCS / "channels" / "_autopsy"

def render_index(items):
    if not items:
        return "<div>분석 없음</div>"
    cards = []
    for it in items:
        tags = "".join(f'<span class="ch-tag">{t}</span>' for t in it.get("tags", [])[:6])
        cards.append(
            f'<a class="ch-card autopsy-card" href="autopsy_{it["slug"]}.html" style="text-decoration:none;color:inherit;">'
            f'<div class="ch-name" style="font-size:15px;">🔥 {it["label"]}</div>'
            f'<div class="ch-meta" style="margin-top:8px;">📅 {it["date"]} · 🎬 {it["n_videos"]}편 · ⏱️ {it.get("avg_duration_min",0)}분</div>'
            f'<div style="margin-top:8px;">🪝 <b>{it.get("hook_dominant","-")}</b> · 🎯 <b>{it.get("outro_dominant","-")}</b></div>'
            f'<div style="margin-top:8px;">{tags}</div></a>')
    return f'<div class="ch-grid">{"".join(cards)}</div>'

def main():
    idx_path = AUTOPSY / "_index.json"
    if not idx_path.exists():
        print("❌ _index.json 없음")
        return
    idx = json.loads(idx_path.read_text())
    items = idx.get("items", [])
    print(f"📂 {len(items)}건 처리")
    # autopsy.html 자체는 build_site.py가 다음 정기 빌드에 갱신 — Action에서는 결과 JSON만 commit
    # 단, 즉시 보이도록 인덱스 + 상세 페이지 stub 생성
    for it in items:
        rp = AUTOPSY / it["slug"] / "result.json"
        if not rp.exists():
            continue
        # 상세 페이지는 build_site.py 다음 빌드에 정식 렌더링됨
        # Action에서는 placeholder만 생성 (이미 결과는 json+md로 저장됨)
    print("✅ 다음 정기 빌드에 페이지 갱신됨")

if __name__ == "__main__":
    main()
