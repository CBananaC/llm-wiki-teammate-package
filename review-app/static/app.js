const drawer = document.querySelector("#bridge-drawer");
const drawerTitle = document.querySelector("#drawer-title");
const drawerBody = document.querySelector("#drawer-body");

async function api(path, options) {
  const res = await fetch(path, options);
  const data = await res.json();
  if (!res.ok || data.error) throw new Error(data.error || res.statusText);
  return data;
}

function openDrawer(title, html) {
  drawerTitle.textContent = title;
  drawerBody.innerHTML = html;
  drawer.classList.add("open");
  drawer.setAttribute("aria-hidden", "false");
}

function closeDrawer() {
  drawer.classList.remove("open");
  drawer.setAttribute("aria-hidden", "true");
}

async function showSkills() {
  const skills = await api("/api/skills");
  openDrawer("LLM Wiki Skills", skills.map(s => `
    <section class="drawer-card">
      <div class="card-row">
        <strong>${escapeHtml(s.title || s.slug)}</strong>
        <code>${escapeHtml(s.path)}</code>
      </div>
      <textarea data-slug="${escapeHtml(s.slug)}">${escapeHtml(s.text || "")}</textarea>
      <button data-save-skill="${escapeHtml(s.slug)}" type="button">Save Skill</button>
    </section>
  `).join("") || `<p>No skills found.</p>`);

  drawerBody.querySelectorAll("[data-save-skill]").forEach(btn => {
    btn.onclick = async () => {
      const slug = btn.dataset.saveSkill;
      const text = drawerBody.querySelector(`textarea[data-slug="${CSS.escape(slug)}"]`).value;
      await api(`/api/skills/${encodeURIComponent(slug)}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text}),
      });
      btn.textContent = "Saved";
      setTimeout(() => btn.textContent = "Save Skill", 900);
    };
  });
}

async function showBundles() {
  const bundles = await api("/api/bundles");
  openDrawer("Review Bundles", bundles.map(b => `
    <section class="drawer-card">
      <div class="card-row">
        <strong>${escapeHtml(b.name)}</strong>
      </div>
      <pre>${escapeHtml(JSON.stringify(b.manifest || {}, null, 2))}</pre>
    </section>
  `).join("") || `<p>No review bundles yet. Batch scripts should write to <code>llm-wiki/outputs/review-bundles/</code>.</p>`);
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

document.querySelector("#open-app").onclick = () => {
  window.open("/app", "_blank", "noopener");
};
document.querySelector("#toggle-skills").onclick = () => showSkills().catch(err => alert(err.message));
document.querySelector("#toggle-bundles").onclick = () => showBundles().catch(err => alert(err.message));
document.querySelector("#drawer-close").onclick = closeDrawer;
