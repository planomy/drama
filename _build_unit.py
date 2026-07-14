#!/usr/bin/env python3
"""Build finding-your-voice.html in the Teach curriculum unit template style."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STYLE_SRC = Path("/tmp/re_style.css")
RUNTIME_SRC = Path("/tmp/re_runtime.js")

LESSONS = [
  {
    "n": 1, "week": 1, "title": "Elements of Drama Warm-Up",
    "mode": "WHOLE-CLASS",
    "walt": "Identify and use the elements of drama through online drama games.",
    "img": "images/unit/04-lesson-01.jpg",
    "success": [
      "I can name at least three elements of drama.",
      "I can use two elements in a short improvisation.",
    ],
    "wp": [
      ("role", "who you are pretending to be"),
      ("situation", "where you are and what is happening"),
      ("voice", "tone, pace and volume"),
      ("tension", "suspense that keeps us hooked"),
    ],
    "brain": [
      "Which element makes a freeze frame feel dramatic?",
      "How can voice alone change the mood of one line?",
      "Why does drama need contrast?",
    ],
    "sequence": [
      ("8 min · Warm-up", "Camera Freeze — celebration, storm, mystery poses. Gallery view + spotlight."),
      ("10 min · Teach", "Elements mini-lesson with Appendix A."),
      ("14 min · Solo build", "30–45 sec moment (mysterious box) using at least two elements."),
      ("8 min · Re-teach", "Spotlight a volunteer; refine voice + tension."),
      ("16 min · Share", "Spotlight shares; class names elements in chat."),
      ("4 min · Wrap", "Exit ticket + preview Lesson 2."),
    ],
    "model": "Perform a 30-sec mini-scene live and narrate how you used voice and tension.",
    "watch": "Drama warm-up & improv games · National Theatre / BBC Teach (~3 min)",
    "exit": ["A. Phone call with fantastic news", "B. Mystery package at the door", "C. Winning a strange competition"],
    "apps": "Appendix A · Elements",
    "notes": "<p><b>Appendix A</b> on screen. Camera Freeze → elements mini-lesson → 30-sec exit ticket.</p>",
  },
  {
    "n": 2, "week": 2, "title": "A Short History of Drama",
    "mode": "WHOLE-CLASS",
    "walt": "Understand how drama has changed across time, and what a monologue and a soliloquy are.",
    "img": "images/unit/05-lesson-02.jpg",
    "success": [
      "I can describe one feature of drama from at least two time periods.",
      "I can explain monologue vs soliloquy.",
    ],
    "wp": [
      ("monologue", "one character speaks to someone or the audience"),
      ("soliloquy", "private thoughts spoken aloud, usually alone"),
      ("chorus", "group that helped tell the story in Greek theatre"),
      ("Globe", "Shakespearean open-air theatre"),
    ],
    "brain": [
      "Why did Greek actors wear masks?",
      "How is a soliloquy different from chatting to a friend on stage?",
      "What stayed the same from Greek theatre to filming at home?",
    ],
    "sequence": [
      ("8 min · Warm-up", "Then & Now poses: Greek, medieval, Shakespearean, modern film star."),
      ("9 min · Teach", "Timeline part 1 (App. B): Ancient Greek & medieval."),
      ("8 min · Quick-fire", "Pose or mime one feature per era + one fact in chat."),
      ("9 min · Teach", "Timeline part 2 + monologue vs soliloquy (App. C)."),
      ("22 min · Character seeds", "Jot 2–3 character ideas for later."),
      ("4 min · Wrap", "Exit ticket + preview Lesson 3 breakouts."),
    ],
    "model": "Say one line twice: monologue (to someone), then soliloquy (private thoughts).",
    "watch": "Shakespeare’s Theatre (the Globe) · BBC Teach (~4 min) · youtube.com/watch?v=D1rbtHchv1g",
    "exit": ["A. Masked Greek actor announces huge news", "B. Soliloquy: alone, deciding something big", "C. Shakespearean town crier"],
    "apps": "Appendices B & C",
    "notes": "<p><b>Appendices B &amp; C</b>. Act the same line both ways.</p>",
  },
  {
    "n": 3, "week": 3, "title": "Drama Across Cultures",
    "mode": "BREAKOUT DEBUT",
    "walt": "Describe how drama communicates ideas and helps continue and revitalise culture.",
    "img": "images/unit/06-lesson-03.jpg",
    "success": [
      "I can describe one way a performance communicated meaning.",
      "I can explain why storytelling matters to a culture.",
    ],
    "wp": [
      ("culture", "shared beliefs, stories and ways of life"),
      ("folktale", "a story passed down through generations"),
      ("trickster", "clever character who outwits a stronger foe"),
      ("revitalise", "bring new life and energy to something"),
    ],
    "brain": [
      "What feelings did the performance communicate?",
      "Why might this story matter to its culture?",
      "Which story pattern could inspire your own piece?",
    ],
    "sequence": [
      ("8 min · Warm-up", "Story Circle — build a class tale one sentence at a time."),
      ("10 min · Teach / watch", "Play storytelling clip; pause for meaning and feeling."),
      ("12 min · First breakouts", "Think-pair-share: meaning + why the story matters."),
      ("8 min · Teach", "App. D patterns — choose character + situation."),
      ("18 min · Narrow it down", "Choose character + situation; note inspiration."),
      ("4 min · Wrap", "Exit ticket. Idea due start of Lesson 4."),
    ],
    "model": "Model answering “what did this communicate?” using App. D patterns.",
    "watch": "Storytelling traditions around the world · TED-Ed / ABC Education",
    "exit": ["A. Opening of a folktale from your culture", "B. Wise elder passing on one lesson", "C. Hero discovers something amazing"],
    "apps": "Appendix D · Characters",
    "notes": "<p><b>Appendix D</b>. First breakout pairs — pin two questions in each room.</p>",
  },
  {
    "n": 4, "week": 4, "title": "Building Your Character",
    "mode": "BREAKOUT PAIRS",
    "walt": "Build a character through role, situation and voice.",
    "img": "images/unit/07-lesson-04.jpg",
    "success": [
      "I can describe my character’s role and situation.",
      "I can find a voice and posture for my character.",
    ],
    "wp": [
      ("hot-seat", "answering questions in role as your character"),
      ("role", "who you are pretending to be"),
      ("want", "what your character desires most"),
      ("posture", "how your body shows the character"),
    ],
    "brain": [
      "What does your character want most right now?",
      "How would they walk into a room?",
      "Which App. F question reveals the most?",
    ],
    "sequence": [
      ("8 min · Warm-up", "Walk As — queen, trickster, giant, animal."),
      ("8 min · Teach", "Demonstrate hot-seating (App. F)."),
      ("20 min · Breakout", "Pairs hot-seat with App. F prompts."),
      ("6 min · Teach", "Turn answers into App. E planning template."),
      ("14 min · Lock it in", "Finalise character, situation and voice."),
      ("4 min · Wrap", "Share one-sentence character + exit ticket."),
    ],
    "model": "Volunteer interviews you in role for ~30 sec.",
    "watch": "Hot-seating: building a character · BBC Bitesize (~3 min)",
    "exit": ["A. Return a faulty product", "B. Voicemail explaining why you’re late", "C. Talk-show intro"],
    "apps": "Appendices E & F",
    "notes": "<p><b>Appendix F</b> hot-seat. Model in role before pairs swap.</p>",
  },
  {
    "n": 5, "week": 5, "title": "Finding Your Moment — Structure & Tension",
    "mode": "BREAKOUT PAIRS",
    "walt": "Combine elements of drama to shape and sustain a one-minute piece.",
    "img": "images/unit/08-lesson-05.jpg",
    "success": [
      "I can choose a key dramatic moment for my piece.",
      "I can plan how tension builds across my piece.",
    ],
    "wp": [
      ("opening", "first line that grabs us"),
      ("turning point", "the peak of the piece"),
      ("contrast", "opposites: loud/quiet, fast/slow"),
      ("focus", "where we point attention"),
    ],
    "brain": [
      "Where is the peak of your story?",
      "What happens if you pause before the big line?",
      "How can stillness create tension?",
    ],
    "sequence": [
      ("8 min · Warm-up", "Tension tableaux — before/after freeze frames."),
      ("10 min · Teach", "One-minute structure (App. G)."),
      ("8 min · Test peak", "Before/after tableaux for your turning point."),
      ("6 min · Teach", "Model pause and contrast on one line."),
      ("24 min · Plan", "Draft structure on planning template."),
      ("4 min · Wrap", "Share lines + exit ticket."),
    ],
    "model": "Deliver one line flat, then with pause + contrast.",
    "watch": "Building tension & using tableaux · BBC Bitesize (~3 min)",
    "exit": ["A. Opening a mysterious box", "B. Countdown before something huge", "C. Waiting for news"],
    "apps": "Appendices E & G",
    "notes": "<p><b>Appendix G</b>. Slow the turning point; use contrast and pause.</p>",
  },
  {
    "n": 6, "week": 6, "title": "Devising the Words & Voice",
    "mode": "BREAKOUT PAIRS",
    "walt": "Use improvisation to devise the words and voice for our piece.",
    "img": "images/unit/09-lesson-06.jpg",
    "success": [
      "I can improvise to find lines for my monologue or soliloquy.",
      "I can use voice to show my character’s feelings.",
    ],
    "wp": [
      ("devise", "create the piece through improvisation"),
      ("tone", "the feeling colour in your voice"),
      ("pace", "how fast or slow you speak"),
      ("volume", "how loud or soft you speak"),
    ],
    "brain": [
      "Which line would you keep from that improv?",
      "How does pace change meaning?",
      "Where should the voice match the turning point?",
    ],
    "sequence": [
      ("8 min · Warm-up", "Voice Swap — same line in three emotions."),
      ("8 min · Teach", "Devising techniques (App. H)."),
      ("22 min · Breakout", "Find and lock lines with a partner."),
      ("6 min · Teach", "Voice toolkit for the turning point."),
      ("12 min · Full run", "Solo run start to finish once."),
      ("4 min · Wrap", "Share a proud line + exit ticket."),
    ],
    "model": "Talk it out live for ~30 sec, then say which line you’d keep.",
    "watch": "Using your voice as an actor · National Theatre (~4 min)",
    "exit": ["A. “We need to talk” three ways", "B. 30-sec rant about a tiny annoyance", "C. Same line, two emotions"],
    "apps": "Appendices H & E",
    "notes": "<p>Improvisation to find words and voice. Keep demos under two minutes.</p>",
  },
  {
    "n": 7, "week": 7, "title": "Performance Skills for the Camera",
    "mode": "BREAKOUT PAIRS",
    "walt": "Use performance skills suited to performing on camera.",
    "img": "images/unit/10-lesson-07.jpg",
    "success": [
      "I can project my voice clearly through the microphone.",
      "I can use facial expression and the camera frame effectively.",
    ],
    "wp": [
      ("framing", "how much of you appears in the shot"),
      ("projection", "clear voice without shouting"),
      ("lens", "where your eyes look on camera"),
      ("gesture", "small, clear moves that read on screen"),
    ],
    "brain": [
      "What ruins an otherwise great performance on camera?",
      "Why does looking at the lens matter?",
      "What one tip would you give a peer?",
    ],
    "sequence": [
      ("8 min · Warm-up", "Frame Test — framing, light, mic."),
      ("10 min · Teach", "On-camera skills: distance, expression, gestures."),
      ("22 min · Solo rehearse", "Rehearse with App. I checklist."),
      ("6 min · Teach", "Peer-tip protocol — kind and concrete."),
      ("10 min · Breakout", "One tip each on framing or voice."),
      ("4 min · Wrap", "Share one improvement + exit ticket."),
    ],
    "model": "Same lines twice: weak frame/flat → strong frame/eyes to lens.",
    "watch": "Acting for camera — tips · StageMilk / BBC Bitesize (~4 min)",
    "exit": ["A. Strongest 30 sec to camera", "B. News report in character", "C. Close-up emotion change"],
    "apps": "Appendix I · Rehearsal checklist",
    "notes": "<p>Model less-effective then more-effective side by side.</p>",
  },
  {
    "n": 8, "week": 8, "title": "Rehearsal & Peer Feedback",
    "mode": "BREAKOUT PAIRS",
    "walt": "Refine our performance using peer feedback and explain how we used elements of drama.",
    "img": "images/unit/11-lesson-08.jpg",
    "success": [
      "I can give a helpful comment using drama vocabulary.",
      "I can explain one element of drama used in my piece.",
    ],
    "wp": [
      ("feedback", "specific, kind comments that help refine"),
      ("element", "one of the 10 drama building blocks"),
      ("effect", "what the choice makes the audience feel"),
      ("refine", "improve a small part with intention"),
    ],
    "brain": [
      "What makes feedback useful?",
      "Which element did you use on purpose?",
      "What will you change after today?",
    ],
    "sequence": [
      ("8 min · Warm-up", "Vocal & physical warm-up + tongue-twister."),
      ("8 min · Teach", "Specific feedback with App. J + App. A."),
      ("26 min · Perform & feedback", "Pairs perform; complete App. J sheet; swap."),
      ("6 min · Teach", "One sentence: element used + effect."),
      ("8 min · Note element", "Write explanation + final tweak."),
      ("4 min · Wrap", "Share feedback used + exit ticket."),
    ],
    "model": "Model vague “good job” vs specific element feedback.",
    "watch": "A powerful short monologue — spot the elements (~2 min)",
    "exit": ["A. Re-record turning point", "B. Director’s note to self", "C. Final line three ways"],
    "apps": "Appendices J & A",
    "notes": "<p><b>Appendix A</b> vocabulary again. Check feedback sheets are completed.</p>",
  },
  {
    "n": 9, "week": 9, "title": "Independent Preparation",
    "mode": "INDEPENDENT",
    "walt": "Finalise and polish our piece, ready for filming.",
    "img": "images/unit/12-lesson-09.jpg",
    "success": [
      "I can perform my piece confidently from memory.",
      "I know how I will film and submit my piece.",
    ],
    "wp": [
      ("finalise", "last polish before filming"),
      ("landscape", "sideways filming orientation"),
      ("take", "one continuous performance take"),
      ("submit", "send the finished film by the agreed method"),
    ],
    "brain": [
      "What still needs polishing?",
      "Where will you film, and how will you light it?",
      "What question will you bring to the help room?",
    ],
    "sequence": [
      ("6 min · Teach", "Goal + share App. K filming guide."),
      ("40 min · Independent", "Rehearse on camera; optional help-room check-ins."),
      ("10 min · Q&A", "Readiness + tech FAQs together."),
      ("4 min · Wrap", "Confirm due date + exit ticket."),
    ],
    "model": "Walk App. K checklist aloud: landscape, light, frame, one full take.",
    "watch": "A student monologue performance (~2 min, teacher-selected)",
    "exit": ["A. Dress-rehearsal strongest 30 sec", "B. Opening into turning point", "C. Final line with contrast"],
    "apps": "Appendices I & K",
    "notes": "<p><b>Appendix K</b>. Keep a help breakout open.</p>",
  },
  {
    "n": 10, "week": 10, "title": "Final Rehearsal, Filming & Reflection",
    "mode": "INDEPENDENT",
    "walt": "Perform our final piece with confidence and reflect on our drama journey.",
    "img": "images/unit/13-lesson-10.jpg",
    "success": [
      "I can perform my piece and sustain my character for one minute.",
      "I can explain how I used elements of drama and what my piece communicates.",
    ],
    "wp": [
      ("sustain", "keep character and focus for the full minute"),
      ("reflect", "think back on what you learned"),
      ("folio", "collection of evidence for assessment"),
      ("audience", "who your piece is speaking to"),
    ],
    "brain": [
      "What are you most proud of?",
      "Which element did the most work in your piece?",
      "What would you try differently next time?",
    ],
    "sequence": [
      ("6 min · Warm-up", "Individual vocal & physical warm-up."),
      ("10 min · Teach", "Final filming tips + submission method."),
      ("35 min · Film & submit", "Film one-minute piece and submit."),
      ("5 min · Celebrate", "Whole-class return — how it felt."),
      ("4 min · Wrap", "Reflection Sheet (App. L)."),
    ],
    "model": "Reconfirm: quiet · landscape · light · upper body · one full take · watch back.",
    "watch": "How to film yourself well at home (~3 min)",
    "exit": ["A. Favourite 30 sec of final piece", "B. Moment you’re proudest of", "C. Director’s wrap speech"],
    "apps": "Appendices K & L",
    "notes": "<p>Celebrate first — then App. L reflection for the folio.</p>",
  },
]

APPENDICES = [
  ("App A — Elements", "images/appendix/slide-02.jpg", "Lessons 1 & 8",
   "The 10 elements: role, situation, movement, space, tension, focus, contrast, voice, time, mood."),
  ("App B — Through time", "images/appendix/slide-03.jpg", "Lesson 2",
   "Greek → medieval → Shakespearean → modern/digital performance."),
  ("App C — Monologue vs soliloquy", "images/appendix/slide-04.jpg", "Lesson 2",
   "Monologue speaks to someone/audience; soliloquy reveals private thoughts alone."),
  ("App D — Characters", "images/appendix/slide-05.jpg", "Lesson 3",
   "Story patterns: race/contest, wise elder, stranger, trickster, loyal animal, sky & earth."),
  ("App F — Hot-seat", "images/appendix/slide-06.jpg", "Lesson 4",
   "Five in-role questions: name/age, want, who matters, problem, feeling now."),
  ("App G — One-minute piece", "images/appendix/slide-07.jpg", "Lesson 5",
   "Opening → build → turning point → final line. Pause. Stillness. Contrast."),
  ("App K — Filming", "images/appendix/slide-08.jpg", "Lessons 9 & 10",
   "Landscape · face a window · upper body in frame · quiet · one full take · watch back."),
]


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
    """function openInfoReport(){
  const i = SLIDES.findIndex(s => (s.nav||'').startsWith('App A'));
  if(i >= 0) show(i);
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
  btn.textContent = '📎 Appendices';
  btn.title = 'Jump to on-screen appendices (I)';
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
    <li><b>Appendices:</b> jump with <kbd>I</kbd> or the Appendices button.</li>
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
          f'<p style="margin-top:10px;font-size:14px;color:#4a5a54"><b>On screen:</b> {lesson["apps"]}</p></div>'
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
          "notes": lesson["notes"],
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
          "notes": lesson["notes"],
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
    chunks.append(
      "SLIDES.push("
      + dumps(
        {
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
                '<p style="margin-top:10px;font-size:14px;color:#4a5a54">Return to the lesson with Jump when done.</p></div>'
              ),
            },
            {
              "k": "brain",
              "q": [
                "What should students notice first?",
                "Which success criterion does this support?",
                "How will you freeze or zoom while teaching from it?",
              ],
            },
          ],
          "notes": f"<p><b>{nav}</b> — {used}. Keep this up while students work.</p>",
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
