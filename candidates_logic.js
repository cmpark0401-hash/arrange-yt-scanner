(function(){
var bar = document.getElementById("candStickyBar");
var countEl = document.getElementById("candStickyCount");
var addBtn = document.getElementById("candStickyAdd");
var addTxt = document.getElementById("candStickyAddText");
var rmBtn = document.getElementById("candStickyRemove");
var rmTxt = document.getElementById("candStickyRemoveText");
function currentTab(){ return document.getElementById("candTabTracked").classList.contains("on") ? "tracked" : "pending"; }
function updateBar(){
  var tab = currentTab();
  if (tab === "tracked") {
    var checked = document.querySelectorAll(".trk-check:checked");
    var n = checked.length;
    countEl.textContent = "📋 선택 " + n + "개 (추적 중)";
    addBtn.style.display = "none"; rmBtn.style.display = "inline-block";
    if (n > 0) { rmBtn.disabled = false; rmBtn.style.opacity = "1"; rmBtn.style.cursor = "pointer"; rmTxt.textContent = n + "개 추적 해제"; }
    else { rmBtn.disabled = true; rmBtn.style.opacity = "0.4"; rmBtn.style.cursor = "not-allowed"; rmTxt.textContent = "해제할 채널 선택"; }
  } else {
    var checked = document.querySelectorAll(".cand-check:checked");
    var n = checked.length;
    countEl.textContent = "📋 선택 " + n + "개 (신규)";
    rmBtn.style.display = "none"; addBtn.style.display = "inline-block";
    if (n > 0) { addBtn.disabled = false; addBtn.style.opacity = "1"; addBtn.style.cursor = "pointer"; addTxt.textContent = n + "개 추적 추가"; }
    else { addBtn.disabled = true; addBtn.style.opacity = "0.4"; addBtn.style.cursor = "not-allowed"; addTxt.textContent = "추가할 채널 선택"; }
  }
}
document.getElementById("candTabPending").addEventListener("click", function(){ setTimeout(updateBar, 50); });
document.getElementById("candTabTracked").addEventListener("click", function(){ setTimeout(updateBar, 50); });
document.querySelectorAll(".cand-check").forEach(function(cb){ cb.addEventListener("change", updateBar); });
document.querySelectorAll(".trk-check").forEach(function(cb){ cb.addEventListener("change", updateBar); });

var PAGE_SIZE = 50; var currentPage = 1; var currentCat = "";
function matchFilter(card){
  if (!currentCat) return true;
  var cats = (card.dataset.catsFilter || "").split("|");
  return cats.indexOf(currentCat) >= 0;
}
function applyDisplay(){
  var allCards = document.querySelectorAll(".cand-card");
  var matched = [];
  allCards.forEach(function(card){ if (matchFilter(card)) matched.push(card); else card.style.display = "none"; });
  var totalPages = Math.max(1, Math.ceil(matched.length / PAGE_SIZE));
  if (currentPage > totalPages) currentPage = totalPages;
  var start = (currentPage - 1) * PAGE_SIZE; var end = start + PAGE_SIZE;
  matched.forEach(function(card, idx){ card.style.display = (idx >= start && idx < end) ? "block" : "none"; });
  renderPagination(totalPages, matched.length);
}
function renderPagination(total, totalItems){
  var pag = document.getElementById("candPagination"); if (!pag) return;
  pag.innerHTML = "";
  if (totalItems === 0) { pag.textContent = "표시할 후보 없음"; return; }
  var info = document.createElement("span");
  info.style.color = "var(--text2)"; info.style.fontSize = "11px"; info.style.marginRight = "10px";
  var s = (currentPage - 1) * PAGE_SIZE + 1;
  var e = Math.min(currentPage * PAGE_SIZE, totalItems);
  info.textContent = s + "~" + e + " / " + totalItems + "개";
  pag.appendChild(info);
  function makeBtn(label, page, disabled, isCurrent){
    var b = document.createElement("button");
    b.textContent = label;
    b.disabled = disabled;
    b.style.padding = "6px 12px"; b.style.borderRadius = "6px"; b.style.fontSize = "12px"; b.style.fontWeight = "700";
    b.style.cursor = disabled ? "not-allowed" : "pointer";
    if (isCurrent) { b.style.background = "var(--primary)"; b.style.color = "#fff"; b.style.border = "1px solid var(--primary)"; }
    else { b.style.background = "var(--surface)"; b.style.color = "var(--text2)"; b.style.border = "1px solid var(--border)"; }
    if (disabled) b.style.opacity = "0.4";
    if (!disabled && !isCurrent) b.addEventListener("click", function(){ currentPage = page; applyDisplay(); window.scrollTo({top:0, behavior:"smooth"}); });
    return b;
  }
  pag.appendChild(makeBtn("← 이전", currentPage - 1, currentPage <= 1));
  var maxPagesShow = 7;
  var startP = Math.max(1, currentPage - 3);
  var endP = Math.min(total, startP + maxPagesShow - 1);
  startP = Math.max(1, endP - maxPagesShow + 1);
  if (startP > 1) { pag.appendChild(makeBtn("1", 1, false, false)); if (startP > 2) { var ell = document.createElement("span"); ell.textContent = "..."; ell.style.color = "var(--text3)"; pag.appendChild(ell); } }
  for (var p = startP; p <= endP; p++) pag.appendChild(makeBtn(String(p), p, false, p === currentPage));
  if (endP < total) { if (endP < total - 1) { var ell2 = document.createElement("span"); ell2.textContent = "..."; ell2.style.color = "var(--text3)"; pag.appendChild(ell2); } pag.appendChild(makeBtn(String(total), total, false, false)); }
  pag.appendChild(makeBtn("다음 →", currentPage + 1, currentPage >= total));
}
document.querySelectorAll(".pend-cat-filter").forEach(function(btn){
  btn.addEventListener("click", function(){
    document.querySelectorAll(".pend-cat-filter").forEach(function(b){
      b.classList.remove("on");
      b.style.background = "var(--surface)"; b.style.color = "var(--text2)";
      b.style.border = "1px solid var(--border)"; b.style.fontWeight = "600";
    });
    btn.classList.add("on");
    btn.style.background = "var(--primary)"; btn.style.color = "#fff";
    btn.style.border = "1px solid var(--primary)"; btn.style.fontWeight = "700";
    currentCat = btn.dataset.cat; currentPage = 1; applyDisplay();
  });
});

applyDisplay();

document.getElementById("candStickyClear").addEventListener("click", function(){
  document.querySelectorAll(".cand-check:checked, .trk-check:checked").forEach(function(cb){ cb.checked = false; });
  updateBar();
});
document.getElementById("candStickySelectTop10").addEventListener("click", function(){
  var sel = currentTab() === "tracked" ? ".trk-check" : ".cand-check";
  var all = document.querySelectorAll(sel);
  for (var i = 0; i < Math.min(10, all.length); i++) all[i].checked = true;
  updateBar();
});

rmBtn.addEventListener("click", function(){
  var checked = document.querySelectorAll(".trk-check:checked");
  if (!checked.length) return;
  var lines = ["### 채널 일괄 추적 해제 (" + checked.length + "개)", ""];
  checked.forEach(function(cb){
    var card = cb.closest(".trk-card"); if (!card) return;
    lines.push("- 이름: " + card.dataset.channel);
    lines.push("  URL: " + card.dataset.url);
    lines.push("");
  });
  var title = "[remove-channels] " + checked.length + "개 채널 추적 해제";
  var url = "https://github.com/cmpark0401-hash/arrange-yt-scanner/issues/new?title=" + encodeURIComponent(title) + "&body=" + encodeURIComponent(lines.join("\n")) + "&labels=remove-channel";
  window.open(url, "_blank");
  checked.forEach(function(cb){ var card = cb.closest(".trk-card"); if (card) { card.style.opacity = "0.4"; card.style.borderColor = "var(--danger)"; cb.checked = false; cb.disabled = true; } });
  updateBar();
});

document.getElementById("candStickyAdd").addEventListener("click", function(){
  var checked = document.querySelectorAll(".cand-check:checked");
  if (!checked.length) return;
  var lines = ["### 채널 일괄 추가 (" + checked.length + "개)", ""];
  checked.forEach(function(cb){
    var card = cb.closest(".cand-card");
    if (!card) return;
    lines.push("- 이름: " + card.dataset.channel);
    lines.push("  URL: " + card.dataset.url + "/videos");
    lines.push("  type: " + card.dataset.type);
    lines.push("  categories: " + card.dataset.categories);
    lines.push("");
  });
  var title = "[add-channels] " + checked.length + "개 채널 일괄 추가";
  var url = "https://github.com/cmpark0401-hash/arrange-yt-scanner/issues/new?title=" + encodeURIComponent(title) + "&body=" + encodeURIComponent(lines.join("\n")) + "&labels=add-channel";
  window.open(url, "_blank");
  checked.forEach(function(cb){ var card = cb.closest(".cand-card"); if (card) { card.style.opacity = "0.5"; card.style.borderColor = "var(--hot)"; cb.checked = false; cb.disabled = true; } });
  updateBar();
});

updateBar();

document.querySelectorAll(".cand-reject-btn").forEach(function(btn){
  btn.addEventListener("click", function(e){
    e.preventDefault(); e.stopPropagation();
    var card = btn.closest(".cand-card"); if (!card) return;
    var body = "### 채널 거부\n\n- 이름: " + card.dataset.channel + "\n- URL: " + card.dataset.url;
    var title = "[reject-channel] " + card.dataset.channel;
    var url = "https://github.com/cmpark0401-hash/arrange-yt-scanner/issues/new?title=" + encodeURIComponent(title) + "&body=" + encodeURIComponent(body) + "&labels=reject-channel";
    window.open(url, "_blank");
    card.style.opacity = "0.4"; btn.disabled = true; btn.textContent = "✗ 거부됨";
  });
});
})();
