#!/usr/bin/env python3
"""Build finding-your-voice.html in the Teach curriculum unit template style."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STYLE_SRC = Path("/tmp/re_style.css")
RUNTIME_SRC = Path("/tmp/re_runtime.js")

LESSONS = json.loads((ROOT / "lessons.json").read_text())
# normalize wp tuples
for _L in LESSONS:
  _L["wp"] = [tuple(x) for x in _L["wp"]]

APPENDICES = [
  ("App A — Elements", "images/unit/14-appendix-a.jpg", "Lessons 1 & 8",
   "The 10 elements: role, situation, movement, space, tension, focus, contrast, voice, time, mood."),
  ("App B — Through time", "images/unit/15-appendix-b.jpg", "Lesson 2",
   "Greek → medieval → Shakespearean → modern/digital performance."),
  ("App C — Monologue vs soliloquy", "images/unit/16-appendix-c.jpg", "Lesson 2",
   "Monologue speaks to someone/audience; soliloquy reveals private thoughts alone."),
  ("App D — Characters", "images/unit/17-appendix-d.jpg", "Lesson 3",
   "Story patterns: race/contest, wise elder, stranger, trickster, loyal animal, sky & earth."),
  ("App E — Planning template", "images/unit/18-appendix-e.jpg", "Lessons 4–6",
   "Monologue Planning Template — character, situation, voice, structure and lines."),
  ("App F — Hot-seat", "images/unit/19-appendix-f.jpg", "Lesson 4",
   "Five in-role questions: name/age, want, who matters, problem, feeling now."),
  ("App G — One-minute piece", "images/unit/20-appendix-g.jpg", "Lesson 5",
   "Opening → build → turning point → final line. Pause. Stillness. Contrast."),
  ("App H — Devising", "images/unit/21-appendix-h.jpg", "Lesson 6",
   "Talk it out · partner thought-tracking · record & listen back."),
  ("App I — Rehearsal checklist", "images/unit/22-appendix-i.jpg", "Lessons 7 & 9",
   "Voice, face, framing, gestures, light and background — self-check before peer tips."),
  ("App J — Peer feedback", "images/unit/23-appendix-j.jpg", "Lesson 8",
   "Specific, kind feedback using drama vocabulary + element + effect."),
  ("App K — Filming", "images/appendix/slide-08.jpg", "Lessons 9 & 10",
   "Landscape · face a window · upper body in frame · quiet · one full take · watch back."),
  ("App L — Reflection", "images/unit/24-appendix-klm.jpg", "Lesson 10",
   "Reflection Sheet for the folio — elements used, what the piece communicates, next time."),
]

# First appendix to open for each lesson (I / Appendices button).
LESSON_APPS = {
  1: ["App A — Elements"],
  2: ["App B — Through time", "App C — Monologue vs soliloquy"],
  3: ["App D — Characters"],
  4: ["App F — Hot-seat", "App E — Planning template"],
  5: ["App G — One-minute piece", "App E — Planning template"],
  6: ["App H — Devising", "App E — Planning template"],
  7: ["App I — Rehearsal checklist"],
  8: ["App J — Peer feedback", "App A — Elements"],
  9: ["App K — Filming", "App I — Rehearsal checklist"],
  10: ["App K — Filming", "App L — Reflection"],
}

# Answer / coaching tips for Screen A discussion starters (shown in teacher notes only).
BRAIN_TIPS = {
  "Which element makes a freeze frame feel dramatic?":
    "Tension, focus or contrast — and a clear role/situation. Push students to name the element, not just “it looks cool.”",
  "How can voice alone change the mood of one line?":
    "Same words, different tone/pace/volume: whisper = mystery; rushing = panic; slow + low = threat. Model with one shared line.",
  "Why does drama need contrast?":
    "Contrast (loud/quiet, still/move) wakes the audience and makes the peak land. Without it, everything flattens.",

  "Why did Greek actors wear masks?":
    "Large theatres + one actor playing many roles; masks amplified emotion/character type so the audience could “read” the figure from far away.",
  "How is a soliloquy different from chatting to a friend on stage?":
    "Soliloquy = private thoughts spoken alone (or as if alone). Chatting to a friend is addressed speech/dialogue. The audience hears secrets others don’t.",
  "What stayed the same from Greek theatre to filming at home?":
    "Storytelling with body, voice, role and situation — wanting an audience to feel something. Forms change; holding attention doesn’t.",

  "What feelings did the performance communicate?":
    "Ask for evidence from voice, movement or situation — not one vague word. Sample: fear then relief; pride; playfulness.",
  "Why might this story matter to its culture?":
    "Passes on values, history, humour, warning or belonging. Stories keep culture alive and help communities share who they are.",
  "Which story pattern could inspire your own piece?":
    "Point to App. D: race/contest, wise elder, stranger, trickster, loyal animal, sky &amp; earth. Pick one pattern + their own twist.",

  "What does your character want most right now?":
    "The want drives the minute — e.g. to confess, to win, to escape, to be believed. If the want is weak, tension collapses.",
  "How would they walk into a room?":
    "Posture shows status/mood: chin high vs shoulders hunched; quick vs careful steps. Link the walk to a voice choice.",
  "Which App. F question reveals the most?":
    "Often “What do you want?” or “What’s the problem right now?” — those unlock the dramatic situation.",

  "Where is the peak of your story?":
    "Usually the decision, discovery or confession — about 40–50 sec into a one-minute piece (App. G turning point).",
  "What happens if you pause before the big line?":
    "Pause = focus + tension; the audience leans in. Rushing past it kills the moment.",
  "How can stillness create tension?":
    "Still body + working eyes/breath makes us wait — space and time do the work before voice returns.",

  "Which line would you keep from that improv?":
    "Keep the line that reveals the want or turns the emotion — scrap clever but empty lines.",
  "How does pace change meaning?":
    "Fast = panic/excitement; slow = weight, threat or sadness. Same sentence can flip meaning with pace alone.",
  "Where should the voice match the turning point?":
    "At the App. G peak — change tone/volume/pace there so the audience feels the shift.",

  "What ruins an otherwise great performance on camera?":
    "Dark face (backlit), looking at the preview instead of the lens, mumbling, huge gestures leaving the frame, portrait mode.",
  "Why does looking at the lens matter?":
    "Lens = the audience’s eyes. Looking at your own image breaks connection; eyes-to-lens feels direct.",
  "What one tip would you give a peer?":
    "Model specific tips: “Chin tip down / sit closer / lift volume on the last line / light from the window.” Ban vague “be better.”",

  "What makes feedback useful?":
    "Specific + kind + actionable: name an element and the effect (“Your pause before the confession built tension”). Avoid “good job.”",
  "Which element did you use on purpose?":
    "Name one from App. A and say what it did to the audience — this is folio evidence language.",
  "What will you change after today?":
    "One concrete tweak only (pace at the turning point, framing, opening line). Small refinements stick.",

  "What still needs polishing?":
    "Guide toward: shaky opening, weak peak, mumbling, or rushing past the pause — one priority, not a laundry list.",
  "Where will you film, and how will you light it?":
    "Quiet room, phone in landscape, face a window (light in front), upper body in frame — App. K. Avoid backlight/silhouette.",
  "What question will you bring to the help room?":
    "Encourage tech or structure questions (“Is my turning point clear?” / “Does this fill a minute?”) so help rooms stay purposeful.",

  "What are you most proud of?":
    "Open — celebrate risk and growth. Prompt element language if they only say “I finished.”",
  "Which element did the most work in your piece?":
    "Must name one element + effect (e.g. “Voice: I slowed at the confession so the audience felt the weight”). Folio gold.",
  "What would you try differently next time?":
    "One forward-looking tweak is enough — shows reflective practice for App. L.",

  # Appendix teaching prompts (meta — for the teacher using the slide)
  "What should students notice first?":
    "Lead with the bold idea of this appendix (definition, timeline step, or checklist item) before details.",
  "Which success criterion does this support?":
    "Link aloud to today’s criteria so the appendix feels purposeful, not decorative.",
  "How will you freeze or zoom while teaching from it?":
    "Spotlight one section; hide the rest of the slide with cursor or jump away when the DO block starts.",
}


def discussion_notes(questions: list[str]) -> str:
  items = []
  for i, q in enumerate(questions, 1):
    tip = BRAIN_TIPS.get(
      q,
      "Invite several answers; push students to use drama vocabulary and cite what they saw/heard.",
    )
    items.append(f"<li><b>Q{i}:</b> {q}<br><i>Answer / tip:</i> {tip}</li>")
  return f"<h4>Discussion starters</h4><ul>{''.join(items)}</ul>"


def theme_style(css: str) -> str:
  repls = [
    ("#0a1419", "#140a1e"),
    ("#0f1c24", "#1e1230"),
    ("#15242c", "#2a1a42"),
    ("#f4f7f6", "#fcfaf8"),
    ("#b4c2c6", "#ddd0ec"),
    ("#7a9098", "#a89cb8"),
    ("#1e2c34", "#2a1a42"),
    ("#24353f", "#342450"),
    ("#3d4f58", "#5a4870"),
    ("#1a262e", "#241836"),
    ("#4a9e8e", "#9b6fd4"),
    ("#6bb8a8", "#c8a0ff"),
    ("#7ec4b4", "#e0c0ff"),
    ("#e1f5e6", "#efe4ff"),
    ("#1a3d32", "#2a1840"),
    ("#f9d45d", "#e8b838"),
    ("#ffe082", "#ffe8a0"),
    ("rgba(126,196,180,", "rgba(200,160,255,"),
    ("rgba(107,184,168,", "rgba(200,160,255,"),
  ]
  for a, b in repls:
    css = css.replace(a, b)
  return css + """
  .btn.inforeport{background:linear-gradient(135deg,#9b6fd4,#c8a0ff);color:#1a1028;}
  table.unit-map th:nth-child(4){letter-spacing:.04em;}
"""


def patch_runtime(js: str) -> str:
  js = js.replace(
    "<th>Wk</th><th>#</th><th>Lesson focus</th><th>English work</th><th>You'll learn</th><th>Report work</th>",
    "<th>L</th><th>#</th><th>Focus</th><th>Teach / Do</th><th>You'll learn</th><th>Appendix</th>",
  )
  js = js.replace(
    "<kbd>T</kbd> notes · <kbd>D</kbd> detach · <kbd>A</kbd> assessment · <kbd>I</kbd> InfoReport",
    "<kbd>T</kbd> notes · <kbd>D</kbd> detach · <kbd>A</kbd> assessment · <kbd>I</kbd> appendices",
  )
  js = js.replace(
    "function openInfoReport(){ window.open(INFOREPORT_URL, '_blank', 'noopener'); }",
    """let appendixReturnIdx = null;
function lessonNumFromSlide(s){
  const m = (s?.nav||'').match(/^L(\\d+)/);
  return m ? +m[1] : null;
}
function appsForSlide(s){
  if (s?.appsNav?.length) return s.appsNav;
  const n = lessonNumFromSlide(s);
  if (n && LESSON_APP_MAP[n]) return LESSON_APP_MAP[n];
  return ['App A — Elements'];
}
function openLessonAppendix(nav){
  const s = SLIDES[idx];
  if (!(s.nav||'').startsWith('App ')) appendixReturnIdx = idx;
  const i = SLIDES.findIndex(x => x.nav === nav);
  if (i >= 0) show(i);
}
function backToLesson(){
  if (appendixReturnIdx != null){ show(appendixReturnIdx); appendixReturnIdx = null; }
  else {
    // Fall back to previous non-appendix slide
    for (let i = idx - 1; i >= 0; i--){
      if (!(SLIDES[i].nav||'').startsWith('App ')){ show(i); return; }
    }
  }
}
function openInfoReport(){
  const s = SLIDES[idx];
  if ((s.nav||'').startsWith('App ')){ backToLesson(); return; }
  appendixReturnIdx = idx;
  const targets = appsForSlide(s);
  const i = SLIDES.findIndex(x => targets.includes(x.nav));
  if (i >= 0) show(i);
}""",
  )
  js = js.replace(
    "document.getElementById('backBtn').onclick=closeOverlay;",
    "const _backBtn=document.getElementById('backBtn'); if(_backBtn) _backBtn.onclick=closeOverlay;",
  )
  # Purple-tint cover wash so it matches the theme
  js = js.replace(
    "rgba(6,19,24,.95) 30%, rgba(6,19,24,.45) 70%, rgba(6,19,24,.25)",
    "rgba(20,10,30,.95) 30%, rgba(20,10,30,.45) 70%, rgba(20,10,30,.25)",
  )
  js = js.replace(
    "function syncInfoReportBtn(){}",
    """function syncInfoReportBtn(){
  const btn = document.getElementById('inforeportBtn');
  if(!btn) return;
  const s = SLIDES[idx];
  const onApp = (s.nav||'').startsWith('App ');
  if (onApp){
    btn.textContent = '← Back to lesson';
    btn.title = 'Return to the lesson you left (I)';
    return;
  }
  const apps = appsForSlide(s);
  if (apps.length === 1){
    const short = apps[0].split(' — ')[0];
    btn.textContent = '📎 ' + short;
    btn.title = 'Open ' + apps[0] + ' (I)';
  } else {
    btn.textContent = '📎 Lesson appendices';
    btn.title = 'Open this lesson\\'s appendices (I): ' + apps.join(', ');
  }
}""",
  )
  return js


def dumps(obj) -> str:
  return json.dumps(obj, ensure_ascii=False)


def main() -> None:
  style = theme_style(STYLE_SRC.read_text())
  runtime = patch_runtime(RUNTIME_SRC.read_text())

  chunks: list[str] = []
  chunks.append("const INFOREPORT_URL = '';")
  chunks.append("const ASSESS_TASK_IMG = 'images/unit/02-overview.jpg';")
  chunks.append("const ASSESS_READING_PDF = 'Finding%20Your%20Voice%20Unit.pdf';")
  chunks.append(
    """const ASSESS_TASK = `
<div class="assess-doc">
  <h3>Assessment — Individual 1-minute monologue or soliloquy</h3>
  <div class="assess-task-meta">
    <div class="fld"><b>Format</b>Filmed performance · ~1 minute · landscape</div>
    <div class="fld"><b>Setting</b>Recorded at home · submitted via agreed method</div>
    <div class="fld"><b>Due</b>End of Lesson 10 / published deadline</div>
  </div>
  <p>Students devise and film a one-minute monologue or soliloquy that uses drama elements with intention.</p>
  <table class="assess-steps">
    <tr><th>Exploring &amp; responding</th><th>Creating &amp; making</th><th>Presenting &amp; performing</th></tr>
    <tr>
      <td>Discussion notes (L2–3) · Peer feedback (L8) · Reflection Sheet (L10, App. L)</td>
      <td>Paired devising (L3–8) · Monologue Planning Template (App. E)</td>
      <td>Rehearsal observations (L7–9) · Final filmed piece (L10)</td>
    </tr>
  </table>
  <p class="assess-due">Student-friendly A–E rubric: Appendix M in the unit PDF.</p>
</div>
`;"""
  )
  chunks.append(
    """const ASSESS_READING = `
<div class="assess-doc">
  <p class="assess-open"><a href="Finding%20Your%20Voice%20Unit.pdf" target="_blank" rel="noopener">Open full unit PDF ↗</a></p>
  <div class="assess-pdfFrame"><iframe title="Finding Your Voice unit PDF" src="Finding%20Your%20Voice%20Unit.pdf"></iframe></div>
</div>
`;"""
  )
  chunks.append(
    """const ASSESS_GUIDE = `
<div class="assess-doc">
  <h3>Teaching guide — quick hits</h3>
  <ul>
    <li><b>Rhythm:</b> short TEACH bursts (≤10 min) then DO — keep students performing.</li>
    <li><b>Weeks 1–2:</b> whole-class · <b>Weeks 3–8:</b> breakout pairs · <b>Weeks 9–10:</b> independent + help room.</li>
    <li><b>Exit tickets:</b> 30-sec recorded clips every lesson.</li>
    <li><b>Appendices:</b> from a lesson, press <kbd>I</kbd> or the purple button for <i>that lesson’s</i> appendix — then <b>← Back to lesson</b> (or <kbd>I</kbd> again).</li>
  </ul>
  <h3>Australian Curriculum v9.0 Drama (Years 5–6)</h3>
  <ul>
    <li>Exploring &amp; responding — elements + culture / meaning</li>
    <li>Creating &amp; making — collaborate, improvise, devise</li>
    <li>Presenting &amp; performing — sustain action on camera</li>
  </ul>
</div>
`;"""
  )
  chunks.append("const ASSESS_TAB_BY_NAV = {};")
  chunks.append("const INFOREPORT_NAV = new Set();")
  chunks.append("const TEACHER_NOTES = {};")
  chunks.append(f"const LESSON_APP_MAP = {dumps({str(k): v for k, v in LESSON_APPS.items()})};")
  chunks.append("const SLIDES = [];")

  chunks.append(
    "SLIDES.push("
    + dumps(
      {
        "type": "cover",
        "nav": "Cover",
        "eyebrow": "Year 5/6 Drama · Fully online",
        "title": "Finding Your Voice",
        "sub": "A history of drama and the solo performance — building to your own one-minute monologue.",
        "notes": "<p>Destination: a one-minute monologue filmed at home. Length: 10 × 60-min lessons · Live online + breakouts · Assessment: individual 1-min film.</p><h4>Navigation</h4><ul><li><b>← →</b> · Jump · <b>T</b> notes · <b>A</b> assessment · <b>I</b> appendices · <b>F</b> present</li></ul>",
      }
    )
    + ");"
  )

  rows = []
  meta = [
    (1, "Elements", "Online drama games", "Warm-up → invent → exit", "App. A"),
    (2, "Across time", "History + mono/soliloquy", "Timeline → character seeds", "App. B–C"),
    (3, "Cultures", "Meaning & culture", "First breakouts → choose", "App. D"),
    (4, "Character", "Role, situation, voice", "Hot-seat → plan", "App. E–F"),
    (5, "Structure", "Shape one minute", "Peak → plan structure", "App. G"),
    (6, "Devising", "Words & voice", "Improv → first full run", "App. H"),
    (7, "Camera", "On-camera skills", "Rehearse + peer tips", "App. I"),
    (8, "Feedback", "Refine & explain", "Perform + feedback sheet", "App. J"),
    (9, "Finalise", "Polish for film", "Independent + help room", "App. K"),
    (10, "Perform", "Film & reflect", "Submit + App. L", "App. L–M"),
  ]
  for n, topic, a, b, app in meta:
    rows.append(
      {
        "week": f"L{n}",
        "n": str(n),
        "topic": topic,
        "englishA": a,
        "englishB": b,
        "learn": a,
        "report": app,
      }
    )

  chunks.append(
    "SLIDES.push("
    + dumps(
      {
        "type": "overview",
        "nav": "Unit overview",
        "eyebrow": "Year 5/6 Drama · 10 × 60-min lessons",
        "title": "About this unit",
        "sub": "Teach/Do rhythm · breakouts from Week 3 · filmed one-minute assessment.",
        "rows": rows,
        "notes": "<p>Walk delivery context, lesson rhythm and assessment strands.</p>",
      }
    )
    + ");"
  )

  chunks.append(
    "SLIDES.push("
    + dumps(
      {
        "type": "divider",
        "nav": "Weeks 1–2",
        "eyebrow": "Phase · Exploring",
        "title": "Whole-class launch",
        "goals": [
          "Elements of drama through online games",
          "Drama across time + monologue vs soliloquy",
          "Build confidence before first breakouts",
        ],
        "notes": "<p>Weeks 1–2 stay whole-class.</p>",
      }
    )
    + ");"
  )

  for lesson in LESSONS:
    if lesson["n"] == 3:
      chunks.append(
        "SLIDES.push("
        + dumps(
          {
            "type": "divider",
            "nav": "Weeks 3–8",
            "eyebrow": "Phase · Creating & presenting",
            "title": "Breakout pairs",
            "goals": [
              "First breakouts — culture & character",
              "Devise structure, words and voice",
              "Rehearse for camera with peer feedback",
            ],
            "notes": "<p>Lessons 3–8 run in paired breakouts.</p>",
          }
        )
        + ");"
      )
    if lesson["n"] == 9:
      chunks.append(
        "SLIDES.push("
        + dumps(
          {
            "type": "divider",
            "nav": "Weeks 9–10",
            "eyebrow": "Phase · Independent",
            "title": "Film & reflect",
            "goals": [
              "Independent polish with a help room",
              "Film the one-minute piece",
              "Celebrate and reflect (App. L)",
            ],
            "notes": "<p>Long independent DO blocks + help room.</p>",
          }
        )
        + ");"
      )

    n = lesson["n"]
    success_html = "".join(f"<li>{s}</li>" for s in lesson["success"])
    teach_blocks = lesson.get("teach") or []
    teach_notes = "".join(
      f"<li><b>{t['mins']} · {t['title']}</b><br>{t['body']}"
      + (f"<br><i>Tip:</i> {t['tip']}" if t.get("tip") else "")
      + "</li>"
      for t in teach_blocks
    )
    apps_nav = LESSON_APPS.get(n, ["App A — Elements"])
    apps_btns = "".join(
      f'<button type="button" class="btn inforeport" style="margin:4px 6px 0 0;padding:7px 12px;font-size:13px" '
      f'onclick="openLessonAppendix({json.dumps(nav)})">{nav.split(" — ")[0]}</button>'
      for nav in apps_nav
    )
    notes_a = (
      f"<h4>Learn — Lesson {n}</h4>{lesson['notes']}"
      f"<p><b>Strand:</b> {lesson.get('strand','')} · <b>Mode:</b> {lesson['mode']}</p>"
      f"<h4>Teach (also on Screen B sequence)</h4><ul>{teach_notes}</ul>"
      f"{discussion_notes(lesson['brain'])}"
      f"<h4>Word Work</h4><ul>"
      + "".join(f"<li><b>{t}</b> — {d}</li>" for t, d in lesson["wp"])
      + "</ul>"
      + f"<p><b>Resources:</b> {lesson.get('resources', lesson['apps'])}</p>"
      + f"<p><b>On-screen appendices:</b> {' · '.join(apps_nav)}. Press <kbd>I</kbd> or use the buttons — then <b>← Back to lesson</b>.</p>"
    )
    notes_b = (
      f"<h4>Apply — Lesson {n}</h4>{lesson['notes']}"
      f"<p><b>Mode:</b> {lesson['mode']} · <b>Model:</b> {lesson['model']}</p>"
      f"<h4>Teach reminders</h4><ul>{teach_notes}</ul>"
      f"<p><b>Exit ticket:</b> {' · '.join(lesson['exit'])}</p>"
      f"{discussion_notes(lesson['brain'])}"
    )
    left_a = [
      {"k": "img", "src": lesson["img"], "cap": lesson["title"], "hero": True, "fit": True},
      {"k": "hook", "q": lesson["walt"]},
    ]
    right_a = [
      {"k": "wp", "list": [{"t": a, "d": b} for a, b in lesson["wp"]]},
      {"k": "brain", "q": lesson["brain"]},
      {
        "k": "html",
        "html": (
          '<div class="card cream"><span class="tag do">SUCCESS CRITERIA</span>'
          f'<ul style="margin:8px 0 0 18px">{success_html}</ul>'
          f'<p style="margin-top:12px;font-size:14px;color:#4a5a54"><b>On screen this lesson:</b></p>'
          f'<div style="margin-top:6px">{apps_btns}</div>'
          '<p style="margin-top:10px;font-size:13px;color:#4a5a54">After an appendix, press <kbd>I</kbd> or <b>← Back to lesson</b>.</p></div>'
        ),
      },
    ]
    chunks.append(
      "SLIDES.push("
      + dumps(
        {
          "nav": f"L{n}A — {lesson['title']}",
          "eyebrow": f"Week {lesson['week']} · Lesson {n} · Learn",
          "eyebrowR": f"Lesson {n} · Screen A",
          "title": lesson["title"],
          "screenlbl": "Student screen 1 of 2",
          "wideLeft": True,
          "left": left_a,
          "right": right_a,
          "notes": notes_a,
          "appsNav": apps_nav,
          "assessTab": "task" if n >= 9 else "guide",
        }
      )
      + ");"
    )

    seq_html = "".join(
      f'<div class="row"><div class="num">{i}</div><div><b>{h}</b><span>{d}</span></div></div>'
      for i, (h, d) in enumerate(lesson["sequence"], 1)
    )
    left_b = [
      {
        "k": "html",
        "html": f'<div class="steps"><span class="tag do">DO THIS · LESSON SEQUENCE</span>{seq_html}</div>',
      },
      {
        "k": "html",
        "html": (
          '<div class="card dark"><span class="tag try">TEACHER MODEL · 30 SEC</span>'
          f'<p style="margin-top:10px;color:var(--ink);font-size:15px;line-height:1.45">{lesson["model"]}</p></div>'
        ),
      },
    ]
    right_b = [
      {
        "k": "html",
        "html": (
          '<div class="card cream"><span class="tag read">WATCH · DRAMA IN ACTION</span>'
          f'<p style="margin-top:8px">{lesson["watch"]}</p>'
          '<p style="margin-top:8px;font-size:13px;color:#4a5a54">Teacher: preview the full clip before showing.</p></div>'
        ),
      },
      {"k": "exit", "items": [f"Exit · {e}" for e in lesson["exit"]]},
      {
        "k": "html",
        "html": (
          '<div class="card dark"><span class="tag wow">30-SEC EXIT TICKET</span>'
          f'<p style="margin-top:8px;color:var(--ink);font-size:14px">Record &amp; upload — pick one. Mode: <b>{lesson["mode"]}</b>.</p></div>'
        ),
      },
    ]
    chunks.append(
      "SLIDES.push("
      + dumps(
        {
          "nav": f"L{n}B — Apply",
          "eyebrow": f"Week {lesson['week']} · Lesson {n} · Apply",
          "eyebrowR": f"Lesson {n} · Screen B",
          "title": f"{lesson['title']} — Apply",
          "screenlbl": "Student screen 2 of 2",
          "wideLeft": True,
          "left": left_b,
          "right": right_b,
          "notes": notes_b,
          "appsNav": apps_nav,
        }
      )
      + ");"
    )

  chunks.append(
    "SLIDES.push("
    + dumps(
      {
        "type": "checkpoint",
        "nav": "★ Assessment",
        "eyebrow": "Assessment · Filmed performance",
        "title": "Your one-minute film",
        "sub": "Devise · rehearse · film · submit · reflect. Open Assessment anytime with A.",
        "assessTab": "task",
        "notes": "<p>Use Assessment for strands, PDF and teaching guide.</p>",
      }
    )
    + ");"
  )
  chunks.append(
    "SLIDES.push("
    + dumps(
      {
        "type": "cover",
        "nav": "Keep performing",
        "eyebrow": "End of unit",
        "title": "Lights. Camera. You.",
        "sub": "Every 30-second challenge built toward your own one-minute monologue. Break a leg!",
        "notes": "<p>Celebrate the journey. Reflection sheets still count as folio evidence.</p>",
      }
    )
    + ");"
  )

  for nav, src, used, blurb in APPENDICES:
    sibling_btns = ""
    # Offer jumps to other appendices that share a lesson (e.g. B↔C)
    siblings = []
    for lesson_n, apps in LESSON_APPS.items():
      if nav in apps:
        for a in apps:
          if a != nav and a not in siblings:
            siblings.append(a)
    if siblings:
      sibling_btns = (
        '<p style="margin-top:12px;font-size:13px;color:#4a5a54"><b>Also this lesson:</b></p>'
        + "".join(
          f'<button type="button" class="btn inforeport" style="margin:4px 6px 0 0;padding:7px 12px;font-size:13px" '
          f'onclick="openLessonAppendix({json.dumps(a)})">{a.split(" — ")[0]}</button>'
          for a in siblings
        )
      )
    chunks.append(
      "SLIDES.push("
      + dumps(
        {
          "type": "appendix",
          "nav": nav,
          "eyebrow": f"On-screen appendix · {used}",
          "eyebrowR": "Appendix",
          "title": nav.replace("App ", "Appendix "),
          "screenlbl": used,
          "wideLeft": True,
          "left": [{"k": "img", "src": src, "cap": nav, "hero": True, "fit": True}],
          "right": [
            {
              "k": "html",
              "html": (
                '<div class="card cream"><span class="tag read">USE THIS SLIDE</span>'
                f'<p style="margin-top:10px">{blurb}</p>'
                f'{sibling_btns}'
                '<div style="margin-top:14px">'
                '<button type="button" class="btn primary" style="padding:10px 16px" onclick="backToLesson()">'
                "← Back to lesson</button></div>"
                '<p style="margin-top:8px;font-size:13px;color:#4a5a54">Or press <kbd>I</kbd> — same as the nav button.</p></div>'
              ),
            },
          ],
          "notes": (
            f"<p><b>{nav}</b> — {used}. Keep this up while students work, then <b>← Back to lesson</b>.</p>"
            f"<p>{blurb}</p>"
          ),
        }
      )
      + ");"
    )

  data_js = "\n".join(chunks)

  chrome = """<body>
<div id="app">
  <div id="stageWrap"><div class="slide" id="slide"></div></div>
  <div id="nav">
    <button class="btn" id="prev">← Prev</button>
    <span id="counter">1 / 1</span>
    <select id="jump"></select>
    <button class="btn assess" id="assessBtn">📋 Assessment</button>
    <button class="btn inforeport" id="inforeportBtn" title="Jump to appendices (I)">📎 Appendices</button>
    <button class="btn" id="notesBtn">Teacher notes</button>
    <button class="btn" id="presentBtn" title="Maximise slide for screen share (F · Esc to exit)">⛶ Present</button>
    <button class="btn" id="next">Next →</button>
  </div>
</div>
<aside id="tnotes">
  <header>
    <div><b>Teacher notes</b><span class="slide-label" id="tnotesTitle"></span></div>
    <span>
      <button class="btn" id="detachBtn" type="button">Detach ⧉</button>
      <button class="btn" id="notesClose" type="button">✕</button>
    </span>
  </header>
  <div class="body" id="tnotesBody"></div>
</aside>
<div id="overlay">
  <div class="modal">
    <header>
      <h2>Assessment</h2>
      <div class="tabs">
        <button class="tab active" data-pane="task">Task</button>
        <button class="tab" data-pane="reading">Unit PDF</button>
        <button class="tab" data-pane="guide">Guide</button>
      </div>
      <button class="btn" id="overlayClose" type="button">✕</button>
    </header>
    <div class="content">
      <div class="panelpane active" id="pane-task"></div>
      <div class="panelpane" id="pane-reading"></div>
      <div class="panelpane" id="pane-guide"></div>
    </div>
    <footer>
      <span class="hint">Press A to toggle · Esc to close</span>
      <button class="btn primary" id="backBtn">← Back to my slide</button>
    </footer>
  </div>
</div>
"""

  # Runtime already fills panes + buildJump/show(0); only add overlayClose + sync button.
  boot = """
document.getElementById('overlayClose').onclick = closeOverlay;
syncInfoReportBtn();
"""

  html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Year 5/6 Drama · Finding Your Voice</title>
<style>
{style}
</style>
</head>
{chrome}
<script>
{data_js}

{runtime}
{boot}
</script>
</body>
</html>
"""

  out = ROOT / "finding-your-voice.html"
  out.write_text(html)
  print(f"wrote {out} ({out.stat().st_size:,} bytes, {html.count('SLIDES.push')} slides)")


if __name__ == "__main__":
  main()
