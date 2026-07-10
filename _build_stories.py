import os, json, html as html_module

BASE = r"C:\Users\Saber\mentAImage-website-deploy"

# Load French texts
with open(os.path.join(BASE, "_fr_texts.json"), encoding="utf-8") as _f:
    FR_TEXTS = json.load(_f)

def esc(t):
    return html_module.escape(t)

def make_fr_body(paragraphs):
    # Skip first paragraph (it's the French title, not body content)
    parts = []
    for t in paragraphs[1:]:
        t = t.strip()
        if not t:
            continue
        # Skip separator lines
        if t.startswith("—---") or t.startswith("---"):
            continue
        et = esc(t)
        # Heading heuristic: short line, no trailing period/», starts uppercase, not a quote
        if (len(t) < 90 and not t.endswith('.') and not t.endswith('»')
                and not t.startswith('«') and not t.startswith('"')
                and not t[0].islower() and not t.startswith("http")):
            parts.append(f"<h2>{et}</h2>")
        elif t.startswith('«') or t.startswith('«') or t.startswith('"'):
            parts.append(f"<blockquote><p>{et}</p></blockquote>")
        else:
            parts.append(f"<p>{et}</p>")
    return "\n      ".join(parts)

NAV = """  <nav class="nav" role="navigation" aria-label="Main navigation">
    <div class="nav__inner">
      <a href="/index.html" class="nav__logo-link" aria-label="mentAImage home">
        <img src="/logo.png" alt="mentAImage" class="nav__logo" height="36" />
      </a>
      <div class="nav__links" role="menubar">
        <a class="nav__link" href="/index.html" role="menuitem">Home</a>
        <a class="nav__link" href="/pulsekey.html" role="menuitem">PulseKey&trade;</a>
        <a class="nav__link" href="/monai.html" role="menuitem">Monai&trade;</a>
        <a class="nav__link" href="/about.html" role="menuitem">About</a>
        <a class="nav__link active" href="/neurodiversity-at-work-stories/" role="menuitem">Stories</a>
        <a class="nav__link" href="/contact.html" role="menuitem">Contact</a>
        <a class="nav__link nav__link--lang" href="/fr/" aria-label="Passer en fran&ccedil;ais">FR</a>
        <a class="btn btn-primary nav__cta" href="/contact.html">Request a Demo</a>
      </div>
      <button class="nav__hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
  <div class="nav__mobile" id="mobile-menu" aria-hidden="true">
    <a class="nav__link" href="/index.html">Home</a>
    <a class="nav__link" href="/pulsekey.html">PulseKey&trade;</a>
    <a class="nav__link" href="/monai.html">Monai&trade;</a>
    <a class="nav__link" href="/about.html">About</a>
    <a class="nav__link active" href="/neurodiversity-at-work-stories/">Stories</a>
    <a class="nav__link" href="/contact.html">Contact</a>
    <a class="nav__link nav__link--lang" href="/fr/">FR</a>
    <a class="btn btn-primary" href="/contact.html">Request a Demo</a>
  </div>"""

FOOTER = """  <footer class="footer">
    <div class="container footer__inner">
      <p class="footer__copy">&copy; 2026 MentaImage Inc. &nbsp;&middot;&nbsp; <a href="/privacy.html">Privacy Policy</a> &nbsp;&middot;&nbsp; <a href="/terms.html">Terms of Service</a> &nbsp;&middot;&nbsp; <a href="mailto:privacy@mentaimage.com">privacy@mentaimage.com</a></p>
    </div>
  </footer>"""

SCRIPT = """  <script>
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobile-menu');
    hamburger.addEventListener('click', () => {
      const open = mobileMenu.getAttribute('aria-hidden') === 'false';
      mobileMenu.setAttribute('aria-hidden', open ? 'true' : 'false');
      hamburger.setAttribute('aria-expanded', open ? 'false' : 'true');
    });
  </script>"""

STYLE = """  <link rel="stylesheet" href="/shared.css" />
  <style>
    .story-wrap { max-width: 760px; margin: 0 auto; padding: 56px 24px 96px; }
    .story-hero { background: linear-gradient(135deg, var(--navy) 0%, var(--navy-mid) 100%); color: #fff; padding: 56px 0 48px; }
    .story-hero .container { max-width: 760px; }
    .story-breadcrumb { font-size: 0.82rem; color: var(--teal); margin-bottom: 16px; }
    .story-breadcrumb a { color: var(--teal); }
    .story-hero h1 { font-size: clamp(1.7rem, 4vw, 2.4rem); font-weight: 800; line-height: 1.25; margin-bottom: 14px; color: #fff; }
    .story-meta { font-size: 0.88rem; color: rgba(255,255,255,0.65); }
    .story-meta .tag { background: rgba(0,175,255,0.18); color: var(--teal); border-radius: 20px; padding: 3px 10px; font-size: 0.78rem; font-weight: 700; margin-right: 8px; }
    .story-photo-wrap { max-width: 760px; margin: -40px auto 0; padding: 0 24px; }
    .story-photo-wrap img { width: 100%; max-height: 400px; object-fit: cover; object-position: center top; border-radius: 12px; box-shadow: 0 8px 32px rgba(8,30,47,0.18); }
    .story-photo-placeholder { width: 100%; height: 200px; background: linear-gradient(135deg, var(--navy-mid), var(--teal)); border-radius: 12px; box-shadow: 0 8px 32px rgba(8,30,47,0.18); display: flex; align-items: center; justify-content: center; font-size: 4rem; color: rgba(255,255,255,0.25); }
    .story-photo-blur img { filter: blur(14px); }
    .story-body h2 { font-size: 1.15rem; font-weight: 700; color: var(--navy); margin-top: 40px; margin-bottom: 10px; padding-bottom: 8px; border-bottom: 2px solid var(--cream); }
    .story-body p { margin-bottom: 16px; line-height: 1.75; color: var(--navy-mid); }
    .story-body blockquote { border-left: 4px solid var(--teal); margin: 24px 0; padding: 12px 20px; background: #eef7ff; border-radius: 0 8px 8px 0; color: var(--navy); font-style: italic; line-height: 1.7; }
    .story-body blockquote p { margin-bottom: 0; color: inherit; }
    .story-body ul { padding-left: 22px; margin-bottom: 16px; list-style: disc; }
    .story-body li { margin-bottom: 6px; line-height: 1.7; color: var(--navy-mid); }
    .story-nav { margin-top: 60px; padding-top: 32px; border-top: 2px solid var(--cream); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }
    .story-nav a { color: var(--teal); font-weight: 600; font-size: 0.9rem; }
    .lang-section { margin-top: 60px; padding-top: 32px; border-top: 2px solid var(--cream); }
    .lang-section h2 { font-size: 1rem; font-weight: 700; color: var(--grey-text); margin-bottom: 24px; letter-spacing: 0.04em; text-transform: uppercase; }
  </style>"""

def page(slug, title, tags, photo_html, body_en, body_fr):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | mentAImage&trade;</title>
  <meta name="description" content="A Beneath the Resume story by Elissia Moullas. {title}" />
{STYLE}
</head>
<body>

{NAV}

  <div class="story-hero">
    <div class="container">
      <p class="story-breadcrumb"><a href="/neurodiversity-at-work-stories/">&larr; All Stories</a> &nbsp;&middot;&nbsp; Beneath the Resume</p>
      <h1>{title}</h1>
      <p class="story-meta"><span class="tag">{tags}</span> &nbsp; By Elissia Moullas</p>
    </div>
  </div>

  <div class="story-photo-wrap">
    {photo_html}
  </div>

  <div class="story-wrap">
    <div class="story-body">
      {body_en}
    </div>

    <div class="lang-section">
      <h2>Fran&ccedil;ais</h2>
      <div class="story-body">
        {body_fr}
      </div>
    </div>

    <div class="story-nav">
      <a href="/neurodiversity-at-work-stories/">&larr; All Stories</a>
      <a href="mailto:privacy@mentaimage.com">Share Your Story</a>
    </div>
  </div>

{FOOTER}
{SCRIPT}
</body>
</html>"""

def p(text):
    return f"<p>{text}</p>"

def bq(text):
    return f"<blockquote><p>{text}</p></blockquote>"

def h2(text):
    return f"<h2>{text}</h2>"

# ---------------------------------------------------------------
# STORIES
# ---------------------------------------------------------------

stories = []

# 1 STEVEN ATME
en = "\n      ".join([
    p("When Steven Atme received his autism diagnosis as a child, he and his parents began a shared journey of understanding and growth. That path, built on patience, curiosity, and compassion, later guided him from his first job at McDonald&rsquo;s and his many volunteer roles to the person he is today."),
    p("Working in busy public settings introduced Steven to many people and personalities. While he formed strong bonds with colleagues, he also encountered moments of unkindness from customers. Even so, he focused on learning and growing through each experience."),
    bq("My very first paying job was at McDonald&rsquo;s. It was a different kind of environment, dealing with a lot of backgrounds. I got along with the people very well, but when something was bothering me, I didn&rsquo;t know how to stand up for myself."),
    p("Alongside his paid work, Steven volunteered regularly in residence homes and community spaces such as St. Marguerite, Ch&acirc;teau Westmount, and the Temple Emmanuel Beth Shalom in Westmount, Montreal. There, he helped run a weekly club for stroke patients, serving food and supporting participants with patience and understanding."),
    h2("Discovering Voice and Leadership"),
    p("Now in his thirties, Steven channels his creativity and lived experience into a meaningful career. He works as a musician, performer, and creative arts teacher who helps people of all ages, with and without disabilities, find joy in learning."),
    bq("I teach piano, vocals, and drama. I approach lessons with clients based on their methods of comprehension, their own method of learning and progression. I make learning not just interesting but also a lot of fun."),
    p("His work extends beyond music. As a humanitarian and public speaker, Steven advocates for compassion and dignity in mental health and special needs inclusion. When he hears about someone struggling, he acts immediately."),
    bq("Lives are very important. When things like that happen, I drop everything. I want to meet the person right away. Even when I have an upcoming engagement, the kid is my priority."),
    h2("Finding Balance and Centering Calm"),
    p("Despite his busy schedule, Steven prioritizes balance and rest. When he faces frustration, he centers himself through silence and mindfulness. He walks, cycles, prays, and meditates to clear his mind before calmly addressing the situation."),
    h2("Respecting Identity and Dignity"),
    bq("There is one thing people tend to forget: opinions are not facts. Ask before you jump. Not everybody reacts the same way. There are no right or wrong answers, but better safe than sorry."),
    h2("A Message for Leaders"),
    bq("Don&rsquo;t judge a book by its cover. You have to get to know the person before you even judge. They will surprise you. We&rsquo;re all humans with strong ambitions."),
    h2("Turning Advocacy into Action"),
    p("In July 2025, Steven drafted and submitted a Legislative Article Proposal for Special Needs and Mental Health to Canada&rsquo;s ministers of health, education, higher education, families, and social services in every province and territory. Several provincial governments recognized his proposal and praised the impact of his advocacy."),
    bq("My message is rooted in hope, faith, and love for all people, especially those facing unique challenges. We&rsquo;re all here on this earth for a reason."),
])
fr = make_fr_body(FR_TEXTS["Steven Atme"])
stories.append(("the-heart-of-advocacy-stevens-story-of-faith-resilience-and-inclusion",
    "The Heart of Advocacy: Steven&rsquo;s Story of Faith, Resilience, and Inclusion",
    "Autism",
    '<img src="/stories/photos/Steven Atme.JPG" alt="Steven Atme" />',
    en, fr))

# 2 AMRRITA CHOPRAA
en = "\n      ".join([
    p("For most of her life, Amrrita Chopraa had no words to explain the challenges she faced. Within the cultural context of India, where she was raised, autism and ADHD were rarely spoken about and awareness was limited. It wasn&rsquo;t until April 2023 that she finally received a formal diagnosis."),
    bq("When I used to hear &lsquo;autism,&rsquo; I thought it was something really big, like cancer or something like that. I never explored it because I thought, &lsquo;I don&rsquo;t have anything like that.&rsquo;"),
    h2("Navigating the Workplace"),
    p("At work, challenges sometimes turned into toxic experiences. Amrrita described having managers who micromanaged her to the point of making her feel unsafe. One supervisor monitored her online status even after leaving the office himself, sending warning messages if she logged off early."),
    bq("I had no guts at that point to say, &lsquo;Stop that, this is not nice.&rsquo; But then another colleague of mine gave me strength and I ended up creating an HR report."),
    h2("Finding Support and Community"),
    p("Despite difficult experiences, Amrrita found strength in supportive networks. At one workplace, she joined a voluntary ADHD support group that met weekly."),
    bq("It was a psychologically safe meeting. Anyone could join. We shared our challenges and sympathized with each other. It was something very validating and supportive."),
    h2("Education and Accommodations"),
    p("Now back in school for an MBA, Amrrita has begun accessing formal accommodations for the first time in her life. Extra time on exams and the ability to record lectures have made a dramatic difference."),
    bq("Now I feel the game is fair. I have enough time to think when I&rsquo;m writing exams."),
    h2("A Message for the Future"),
    bq("It&rsquo;s still a big taboo. People think about neurodivergence in a negative way, they think we only have challenges. They don&rsquo;t see our talent that is different from others. I always feel, is it safe to share? Will I be judged? I&rsquo;m thinking that we are special in the best possible way."),
])
fr = make_fr_body(FR_TEXTS["Amrrita Chopraa"])
stories.append(("special-in-the-best-possible-way-amrritas-story",
    "Special in the Best Possible Way: Amrrita&rsquo;s Story",
    "Autism &middot; ADHD",
    '<img src="/stories/photos/Amrrita Chopraa.JPG" alt="Amrrita Chopraa" />',
    en, fr))

# 3 COLIN MURPHY
en = "\n      ".join([
    p("For years, Colin Murphy sensed he processed information differently. Diagnosed with dyslexia at around age 12, he has lived with it for nearly three decades. In recent years, he has also recognized traits of ADHD in himself."),
    bq("They limited the diagnosis to just dyslexia, but I kind of wish that they&rsquo;d done a more thorough diagnosis because I think they missed something there."),
    h2("First Jobs, Real Friction"),
    p("With a background in chemistry, Colin started out in pharmaceutical labs. He learned quickly and loved new challenges, yet unstructured work stretched his working memory. Writing added another layer of challenge."),
    bq("Even though I then went on to get a PhD and write academic articles, if I&rsquo;m very tired, I can&rsquo;t spell my own name."),
    h2("Building Systems that Work"),
    p("Colin&rsquo;s current role is in process improvement, optimization, and automation. He uses noise-cancelling gear in overstimulating environments and designs visual task boards with daily, weekly, and monthly cards."),
    h2("Masks, Energy, and the Social Economy"),
    bq("Often, neurodivergent persons are at a disadvantage, with neurotypical persons better matching social expectations. It takes additional energy above and beyond me to put on the performative mask to align with the majority&rsquo;s social expectations."),
    h2("From Layoff to Atypical Lean"),
    p("After being laid off, Colin founded a consultancy called Atypical Lean, where he uses lean manufacturing principles to build toolkits and training that help businesses become more neuroinclusive."),
    h2("What He Asks of Leaders"),
    p("Colin wants a baseline of knowledge and empathy. He urges leaders to recognize comorbidities, understand masking, stimming, and sensory overload. The goal is simple: reduce the burden on neurodivergent people to conform and build systems where they can contribute without spending extra energy to fit in."),
])
fr = make_fr_body(FR_TEXTS["Colin Murphy"])
stories.append(("finding-clarity-turning-a-dyslexia-journey-into-a-blueprint-for-change",
    "Finding Clarity: Turning a Dyslexia Journey into a Blueprint for Change",
    "Dyslexia &middot; ADHD",
    '<img src="/stories/photos/Colin Murphy.png" alt="Colin Murphy" />',
    en, fr))

# 4 DEBORAH SHUKYN-PLAGEMAN
en = "\n      ".join([
    p("Deborah Shukyn-Plageman&rsquo;s understanding of her own neurodivergence came late in life. She was formally diagnosed with autism, ADHD and identified as twice exceptional at the age of 60."),
    bq("Now, I&rsquo;m in possession of my diagnosis and I have control over where it lands in the medical system. And when my cognition is not at its best later in life, it&rsquo;s critically important to me that I&rsquo;m in possession of my records."),
    h2("Workplaces That Loved Her, and Then Hurt Her"),
    p("Across her career, patterns emerged that were harder to reconcile. Deborah encountered repeated moments of moral injury, situations where her values clashed with workplace practices in ways she could not ignore."),
    bq("For me, that doesn&rsquo;t compute. Either you&rsquo;re telling me I&rsquo;m doing well, and my performance appraisal matches that, or I&rsquo;m not doing well."),
    h2("Choosing to Build Something Different"),
    p("Thirteen years ago, following a layoff, Deborah built PersonaGrata, a consultancy that allowed her to design work around her body, mind, and values. Today, she coaches neurodivergent individuals, trains other coaches in neuro-affirming practices, and works with leaders navigating neurodiversity in the workplace."),
    bq("On balance, I have never really felt accepted or supported to do my best work until now, until I created my best work."),
    h2("Well-Being and Sustainable Work"),
    p("When her work shifted fully online during COVID-19, Deborah experienced a profound improvement in her health and quality of life. For years, she had been told remote work was impossible, only to watch it become rapidly normalized."),
    h2("Vision for Neuro-Affirming Workplaces"),
    bq("What you would do for us would make every human&rsquo;s life better in the context of work."),
    p("To learn more about Deborah and her work, visit <a href='https://www.personagrataconsulting.com/'>personagrataconsulting.com</a>."),
])
fr = make_fr_body(FR_TEXTS["Deborah Shukyn-Plageman"])
stories.append(("listening-for-the-voices-we-miss-deborahs-journey",
    "Listening for the Voices We Miss: Deborah&rsquo;s Journey Through Neurodivergence and Self-Designed Leadership",
    "Autism &middot; ADHD &middot; Twice Exceptional",
    '<img src="/stories/photos/Deborah Shukyn-Plageman.png" alt="Deborah Shukyn-Plageman" />',
    en, fr))

# 5 GILLIAN FORTH
en = "\n      ".join([
    p("Gillian Forth&rsquo;s story with neurodiversity began when she was seventeen, sitting in a psychologist&rsquo;s office and receiving a diagnosis that felt vague and strangely disconnected from her lived reality. Years later, as she worked with neurodivergent individuals professionally, she recognized herself in the people she was supporting."),
    bq("As I gained a greater understanding of different neurodivergent identities, it really opened my eyes and resonated deeply."),
    h2("Moral Injury in Mission-Driven Work"),
    p("As she continued through various nonprofit roles, Gillian began to notice a painful disconnect. Organizations that publicly championed values of equity and justice sometimes made internal decisions that contradicted those same values."),
    bq("I think even when we&rsquo;re in environments where there are challenges within the larger organization, our managers can make up for them in many ways. Conversely, unsupportive managers can turn what would otherwise be a good role into an incredibly negative experience."),
    h2("Stepping Into Self-Employment"),
    p("Her practice, The Low Achiever, is a space where she coaches neurodivergent individuals and supports organizations with neuroinclusive practices. Her work is grounded in disability justice, intersectionality, and deep respect for lived experience."),
    h2("What a Neuroaffirming Workplace Looks Like"),
    bq("It&rsquo;s a process. It&rsquo;s something that you create and co-create on a consistent basis. Because people&rsquo;s needs evolve, people&rsquo;s needs change, and they will conflict with each other."),
    h2("The Roots of Ableism"),
    bq("The tip of the iceberg is awareness of disability and creating different kinds of social support or safety nets. When we go deeper under the surface of that iceberg, we&rsquo;re asking questions such as what makes something an accommodation? Who decides what the default workplace is?"),
])
fr = make_fr_body(FR_TEXTS["Gillian Forth"])
stories.append(("shifting-the-default-gillian-on-disability-justice-and-workplace-change",
    "Shifting the Default: Gillian on Disability Justice and Workplace Change",
    "Autism",
    '<img src="/stories/photos/Gillian Forth.JPG" alt="Gillian Forth" />',
    en, fr))

# 6 HANNELORE COECKELBERGHS
en = "\n      ".join([
    p("When Hannelore Coeckelberghs received her autism diagnosis eight years ago, it helped her understand years of workplace challenges that had often left her feeling overwhelmed and unsupported."),
    h2("Early Jobs and Quiet Determination"),
    p("At 22, Hannelore began her first job, a temporary position, entering coordinates into a database. Her determination to complete every task, no matter how monotonous or exhausting, became both a strength and a source of struggle."),
    h2("A Chance Application That Lasted Nine Years"),
    p("Hannelore&rsquo;s next step came unexpectedly. What began as a way to avoid relocating turned into a nine-year job on the night shift. After five years, she was doing a two-person job alone."),
    bq("I always want to finish my job correctly, and I took all the work on me until I couldn&rsquo;t."),
    bq("Things I find hard are calling someone, I literally ran away from the phone, and also speaking in front of a group of people."),
    h2("Finding Support in Family"),
    p("A major turning point came when Hannelore&rsquo;s brother bought a sandblasting company and offered her a role. She&rsquo;s been there ever since."),
    bq("My brother knows about my problems and he really listens. He always suggests solutions to change things. He listens and he respects my limits."),
    h2("Practical Strategies for Self-Care"),
    p("To make her workdays more manageable, Hannelore developed personal strategies. Rather than taking one long break, she spaces out several shorter ones throughout the day."),
    bq("I tattooed &lsquo;limits&rsquo; on my arm. So I often look at it and remind myself to watch my limits and take a break when I need it."),
    h2("A Message to Employers"),
    bq("To listen and to respect limits and boundaries. Especially to listen. When someone says, &lsquo;I can&rsquo;t do this,&rsquo; don&rsquo;t push it. Take it seriously. Just because we do our job well and make it look easy, doesn&rsquo;t mean it is."),
    bq("There are always people who can help you, but you have to dare to speak. And even if they don&rsquo;t listen, don&rsquo;t give up. Just remember that there&rsquo;s always someone who will eventually listen."),
])
fr = make_fr_body(FR_TEXTS["Hannelore Coeckelberghs"])
stories.append(("respecting-limits-hannelores-journey-toward-sustainable-work",
    "Respecting Limits: Hannelore&rsquo;s Journey Toward Sustainable Work",
    "Autism",
    '<div class="story-photo-placeholder">&#9787;</div>',
    en, fr))

# 7 JON MICK
en = "\n      ".join([
    p("From a young age, Jon Mick knew he wanted to be a consultant. By the time he entered college, Jon had already launched his own consulting company. That drive led him to a major consulting firm right out of school, where long hours and frequent travel became his norm."),
    h2("Understanding His Diagnoses"),
    p("Jon describes himself as twice exceptional: moderately autistic, gifted, and living with ADHD inattentive type. This clarity helped him make sense of long-standing struggles with communication, focus, and burnout."),
    bq("I often felt the tension of needing to make big, impactful changes at work that required deep thinking. But most environments wanted quick answers. I struggled with breaking down complex solutions into something leadership could digest."),
    bq("Back then, I thought I was just broken or stupid. But that didn&rsquo;t align with all of my hard work."),
    h2("A Cycle of Burnout"),
    p("Jon&rsquo;s career unfolded in cycles of high achievement followed by exhaustion. The pattern repeated: after roughly a year of intense dedication, burnout set in."),
    bq("Burnout isn&rsquo;t just from working too hard, it&rsquo;s from being misaligned with values and your work style. You can sometimes fall into that trap of feeling like you just need to work harder, and I think that only contributes further to burnout."),
    h2("Creating Space for Others"),
    p("As a director of product management during COVID-19, Jon introduced weekly surveys for his team to track engagement and mental health."),
    bq("If we didn&rsquo;t have an engaged and healthy team, we weren&rsquo;t going to succeed."),
    h2("Looking Forward"),
    p("Today, Jon continues to balance entrepreneurship with his current work. He has embraced transparency with his employer, openly disclosing his neurodivergence to his manager. His motivation was not only to seek support for himself but also to raise awareness and create space where others could feel understood."),
])
fr = make_fr_body(FR_TEXTS["Jon Mick"])
stories.append(("balancing-innovation-and-burnout-jons-story",
    "Balancing Innovation and Burnout: Jon&rsquo;s Story",
    "Autism &middot; ADHD &middot; Twice Exceptional",
    '<div class="story-photo-placeholder">&#9786;</div>',
    en, fr))

# 8 KELLY C
en = "\n      ".join([
    p("It wasn&rsquo;t until the age of 40 that Kelly C, a DevOps Engineer at Loop Earplugs, finally received the diagnoses that made sense of a lifetime of internal contradictions: Autism Level 1 and ADHD, combined type. Before that, there had been a revolving door of labels including borderline personality disorder, generalized anxiety disorder, even &ldquo;hysteria.&rdquo;"),
    bq("ADHD is for boys. My only reference point had been a classmate who couldn&rsquo;t sit still. I don&rsquo;t do that."),
    p("Her boss pointed out that she did, just not in the same way: chaotic, not focused on a single thing, switching tasks a lot. That led her to seek a formal assessment. When she disclosed her diagnosis, her new manager responded very differently, and she was eventually fired."),
    h2("Thriving at Loop: A Workplace That Listens"),
    p("Today, Kelly works at Loop Earplugs. There are support dogs, silent booths, fidget toys, and a workplace budget you can use to buy noise-canceling headphones. One of the founders told her: &ldquo;Do not change how you are, because it&rsquo;s just wonderful.&rdquo;"),
    bq("If I have a very bad day, I can just say, Look, I&rsquo;m going to log off. And I&rsquo;ll catch up a few hours later."),
    h2("Living Without a Mask"),
    p("Kelly is proudly open about being neurodivergent, queer, and deaf in one ear; not out of obligation, but because she hopes her story will help others feel less alone."),
    bq("If it helps one person, it was all worth it."),
    h2("Rewriting the Narrative"),
    bq("Since I&rsquo;ve been diagnosed, I also understand myself a lot better. I haven&rsquo;t done self-harm since then. So I&rsquo;m doing a lot better in dealing with my explosive moments."),
    h2("A Message for Others"),
    bq("We&rsquo;re not broken. We&rsquo;re not hysterical. We mask because it is expected of us, and it&rsquo;s fucking tiring. We are worthy. Period. We are enough."),
])
fr = make_fr_body(FR_TEXTS["Kelly Crabbé"])
stories.append(("from-burnout-to-belonging-kellys-journey-with-neurodivergence",
    "From Burnout to Belonging: Kelly&rsquo;s Journey with Neurodivergence in the Workplace",
    "Autism &middot; ADHD",
    '<img src="/stories/photos/Kelly Crabbé.JPG" alt="Kelly C" style="object-position: center center;" />',
    en, fr))

# 9 LOUISE LEROY
en = "\n      ".join([
    p("Meet Louise Leroy, an IT Consultant at Passwerk. When Louise was diagnosed with autism in 2018, it brought clarity but not immediate answers. The pattern repeated itself: she&rsquo;d begin a role, feel overwhelmed, and either resign or be asked to leave."),
    bq("It wasn&rsquo;t very easy. There were always too many people, too much noise, too many things happening at once. It was just&hellip; too much for me."),
    bq("I had no confidence in myself."),
    h2("A Place that was Just Right"),
    p("Everything began to shift when Louise joined Passwerk, a Belgian company that hires autistic professionals and supports them in finding long-term, meaningful work. At Passwerk, each consultant is paired with a job coach."),
    bq("I have already been working there for four years. It&rsquo;s a big change from the few days I used to work in my previous jobs. If I encounter a difficulty, I can always communicate it to my job coach. And she will do everything to try to help me."),
    bq("I feel very comfortable talking about issues related to my diagnosis and accommodations. So, I feel good at my job right now."),
    h2("Creating Space for Difference"),
    bq("It&rsquo;s important to know that for many autistic people, communication and social interactions can be difficult. That doesn&rsquo;t mean we&rsquo;re not trying. I do my best to work well, but I might not always know how to express what I need."),
    bq("Sometimes people expect you to act a certain way, to be very social, to talk a lot. But not everyone is like that. And that should be okay."),
    h2("Finding Her Place"),
    bq("I found a job that helped me regain my confidence. Before this, I didn&rsquo;t believe in myself."),
])
fr = make_fr_body(FR_TEXTS["Louise Leroy"])
stories.append(("it-was-just-too-much-louises-journey-to-finding-a-workplace-that-works",
    "&ldquo;It Was Just Too Much&rdquo;: Louise&rsquo;s Journey to Finding a Workplace That Works",
    "Autism",
    '<img src="/stories/photos/Louise Leroy.JPG" alt="Louise Leroy" />',
    en, fr))

# 10 MANSHUK KEREY
en = "\n      ".join([
    p("For Manshuk Kerey, a certified HR Specialist with international expertise, understanding neurodiversity didn&rsquo;t begin with her own diagnosis, but with her son&rsquo;s. When her son was formally diagnosed with ADHD, the experience became a mirror."),
    bq("He&rsquo;s a copy of me behaviorally. When I was his age, I didn&rsquo;t struggle academically, but I did struggle with behaviors that weren&rsquo;t well understood back then."),
    bq("Looking back, I see why so many neurodivergent people shine so brightly. When we care about something, we go deep and perform at a very high level. Interest drives excellence."),
    h2("A Career Interrupted"),
    p("After moving to Canada and earning a graduate diploma from McGill University, Manshuk joined a global financial firm. When remote work began during COVID, the pressure intensified. She was eventually let go for &ldquo;lack of attention to detail&rdquo;, a decision that caught her by surprise."),
    bq("After months of consistent performance and never requesting time off, I believed my reliability was clear. However, in the absence of trust, even minor technical issues can be misinterpreted as a lack of engagement."),
    h2("Redefining Success Through Entrepreneurship"),
    p("In 2022, Manshuk launched Phrcert.com, a platform designed to make HR certification preparation accessible to real professionals, especially those balancing demanding jobs, family responsibilities, and neurodivergent thinking styles."),
    bq("When I create content, I think of people like me and my son. We need resources that are structured but flexible, challenging but achievable, and always clear."),
    h2("A Message to Employers"),
    bq("Employees shouldn&rsquo;t need a doctor&rsquo;s note to deserve flexibility. We should review every request with empathy and create cultures where people feel safe to ask for what they need. When leaders model empathy and transparency, the entire culture shifts. Inclusion starts at the top."),
    p("Learn more at <a href='https://www.phrcert.com'>phrcert.com</a>."),
])
fr = make_fr_body(FR_TEXTS["Manshuk Ahmetzhan"])
stories.append(("a-diagnosis-in-progress-manshuk-on-neurodiversity-and-entrepreneurship",
    "A Diagnosis in Progress: Understanding Begins at Home",
    "ADHD",
    '<img src="/stories/photos/Manshuk Ahmetzhan.png" alt="Manshuk Kerey" />',
    en, fr))

# 11 MARISA MCCLURE
en = "\n      ".join([
    p("Meet Marisa McClure, a Case Worker at Big Brothers Big Sisters of West Island. Diagnosed with ADHD in 2016 and later with dyspraxia and dyscalculia in 2021, Marisa&rsquo;s neurodivergence shapes how she navigates the world."),
    bq("Dyscalculia is kind of like dyslexia but with numbers. I can&rsquo;t do math in my head or visualize numbers in my head. So with phone numbers, I have to say them out loud otherwise they get jumbled up in my head."),
    h2("&ldquo;It Itched My Brain in the Right Way&rdquo;"),
    p("Marisa&rsquo;s first job as a lifeguard wasn&rsquo;t what she had hoped. Things changed when she took a fast-paced job at a fast-food chain."),
    bq("It was stressful, but to me I loved it because it was itching my brain in the right way. I loved the quick-pace, the multitasking. Even when it was hectic, I&rsquo;d leave work thinking, That was fun."),
    h2("A Place That Saw Her"),
    p("Everything changed when Marisa joined a small clinic with a compassionate and open-minded team."),
    bq("I didn&rsquo;t feel like just an employee, I feel like they got me. Being understood is a big thing for me because my whole life being neurodivergent I feel like I over explain myself all the time because people don&rsquo;t understand."),
    h2("Advocacy and Openness"),
    bq("Something that really helped me cope was talking to people about the fact that I have ADHD. Trying to advocate for myself, explaining the accommodations I need and being more outspoken helped because most of the time employers are willing to accommodate you or hear you out at least."),
    h2("Thriving Starts with Being Seen"),
    bq("I wish more employers knew the strengths that come with being neurodivergent. Neurodivergent people are very creative and detail oriented, so I wish that they realized that it is a positive to have new perspectives on your team."),
])
fr = make_fr_body(FR_TEXTS["Marisa McClure"])
stories.append(("they-finally-saw-me-marisas-journey-with-neurodivergence",
    "&ldquo;They Finally Saw Me&rdquo;: Marisa&rsquo;s Journey with Neurodivergence in the Workplace",
    "ADHD &middot; Dyspraxia &middot; Dyscalculia",
    '<img src="/stories/photos/Marisa McClure.jpeg" alt="Marisa McClure" />',
    en, fr))

# 12 NAT HAWLEY
en = "\n      ".join([
    p("Nat Hawley&rsquo;s story begins long before they had the language to describe neurodiversity or inclusion. Diagnosed with autism and dyspraxia around the age of three or four, and later with dyslexia at sixteen, they grew up in a world that often misunderstood how they learned and communicated."),
    bq("I remember often feeling &lsquo;about two years behind&rsquo; my peers. At the same time, I was deeply curious and motivated to explore the world."),
    h2("The Reality of Psychometric and AI Screening"),
    bq("There&rsquo;s a right or wrong answer to having a personality. And if your personality doesn&rsquo;t line up with what they think is good, then you fail."),
    h2("Moments of Support and What Inclusive Leadership Looks Like"),
    bq("If you follow the status quo, and you&rsquo;re just looking at a checklist of what &lsquo;good&rsquo; looks like, neurodivergent people often fall short. But if you actually look at the quality of the work, rather than the quantity, things change."),
    h2("Building Divergent Thinking"),
    p("Nat Hawley, MSc (Applied Neuroscience), is the founder of Divergent Thinking, an independent neurodiversity consultancy. His work is led and delivered by facilitators with lived experience. He has delivered over 350 sessions across sectors."),
    h2("What a Neuroaffirming Workplace Looks Like"),
    bq("There&rsquo;s never going to be a perfect workplace, but people have to be willing to be continuously adapting, tweaking and making changes. They need to understand why they&rsquo;re making the changes. You&rsquo;re not doing it just because I&rsquo;m complaining and I&rsquo;m being difficult, you&rsquo;re doing it because you benefit. When I succeed, you succeed, and when you succeed, I succeed."),
    p("Learn more at <a href='https://www.divergentthinking.uk'>divergentthinking.uk</a>."),
])
fr = make_fr_body(FR_TEXTS["Nat Hawley"])
stories.append(("beyond-equality-nat-on-neurodiversity-and-equity-at-work",
    "Beyond Equality: Nat on Neurodiversity and Equity at Work",
    "Autism &middot; Dyspraxia &middot; Dyslexia",
    '<img src="/stories/photos/Nat Hawley.png" alt="Nat Hawley" />',
    en, fr))

# 13 PAUL SHERMAN
en = "\n      ".join([
    p("Paul Sherman was 62 when the pieces of his life finally clicked into place. In 2018, he received a diagnosis of Autism Level 1. &ldquo;It was a very late diagnosis,&rdquo; he says, reflecting on a career that spanned military service, working as an electronics technician, and biomedical/clinical engineering."),
    bq("Nobody had any clue about autism, basically. It took a long time to sort out what my struggles were, what parts of my struggles were due to autism, what problems were due to the house I grew up in."),
    h2("Struggles in Civilian Jobs"),
    p("After completing his military service, Paul became an electronics technician. One major issue for him was sales."),
    bq("I knew those extended warranties weren&rsquo;t a good deal for the customer. I couldn&rsquo;t promote it."),
    h2("Building a Career Through Engineering"),
    p("Paul earned a degree in electrical engineering and worked for over two decades as a biomedical engineer. His hyper-focus, technical insight, and out-of-the-box thinking finally had room to thrive. He created a custom medical system to support veterans with spinal cord injuries that was presented at a national conference."),
    bq("At one point, my big boss in Washington, DC told me, &lsquo;You&rsquo;re our trailblazer.&rsquo;"),
    h2("What Paul Wishes More People Understood"),
    p("Paul&rsquo;s insights into what makes or breaks a workplace for neurodivergent people are clear: be honest with us, give us time to process difficult questions, respect our sensory environment, don&rsquo;t give us ten projects at once, and don&rsquo;t micromanage."),
    h2("Looking Back with Clarity"),
    bq("If I had known I was autistic back when working, perhaps we could have worked something out. Some of the bad things that happened wouldn&rsquo;t have happened. But knowing now, I&rsquo;m eager to help others avoid what I went through."),
])
fr = make_fr_body(FR_TEXTS["Paul Sherman"])
stories.append(("from-rigidity-to-realization-pauls-path-as-a-late-diagnosed-autistic-professional",
    "From Rigidity to Realization: Paul&rsquo;s Path as a Late-Diagnosed Autistic Professional",
    "Autism",
    '<div class="story-photo-placeholder">&#9788;</div>',
    en, fr))

# 14 ROGER JONES (MARK SONES)
en = "\n      ".join([
    p("When Roger Jones received his diagnoses of Autism Spectrum Disorder Level 1 and ADHD (inattentive type), it was like the missing puzzle piece finally fell into place."),
    bq("My brain tends to buzz with many different thoughts simultaneously, often completely separate from what&rsquo;s happening around me."),
    h2("The Unspoken Rules"),
    p("As Roger moved into analyst and product management roles in the tech industry, his career seemed promising. Yet over time, he began to notice an invisible barrier. Promotions often went to those who excelled at self-promotion and networking rather than those who quietly delivered results."),
    bq("There&rsquo;s kind of the expectation that people will act in a certain way, and those aren&rsquo;t clear. We&rsquo;re generally not aware until well after the fact."),
    h2("Burnout and Betrayal"),
    p("One of Roger&rsquo;s most difficult periods came at a rapidly growing tech company where he managed a team overseeing 40 engineers. Working 70 to 80 hours a week without the promotion or recognition he sought left him drained."),
    bq("I eventually burnt out and left. Recovery took nine months."),
    h2("From Struggle to Advocacy"),
    p("After leaving that role, Roger pursued an MBA. During the program, his autism diagnosis reframed his entire career."),
    bq("I don&rsquo;t want other neurodivergent people to have to go through what I&rsquo;ve been through for the last 15 years."),
    h2("A Call to Leaders"),
    bq("All our lives we&rsquo;ve been trying to change ourselves to fit your expectations, to fit into your world. Everybody else gets to show up as themselves, but we cannot. We&rsquo;ve been putting in 100% of the effort to make this relationship work all this time and many of us are saying &lsquo;no longer.&rsquo; It&rsquo;s time that the 80% of the population that is neurotypical put in some of the work."),
])
fr = make_fr_body(FR_TEXTS["Mark Sones"])
stories.append(("from-burnout-to-advocacy-for-neuroinclusion-rogers-story",
    "From Burnout to Advocacy for Neuroinclusion: Roger&rsquo;s Story",
    "Autism &middot; ADHD",
    '<div class="story-photo-blur"><img src="/stories/photos/Mark Sones.jpg" alt="Roger Jones" /></div>',
    en, fr))

# 15 ROBERT SCHMUS
en = "\n      ".join([
    p("Robert &ldquo;Bob&rdquo; Schmus was diagnosed with autism and ADD at the age of 15. Now in his late 30s, he works as a licensed clinical social worker and speaks openly about his neurodivergence in the context of his professional life and the work he has chosen to pursue."),
    h2("The Pain of Being Dismissed"),
    p("In 2016, Bob stepped into a clinical team leader role at a residential home for neurodivergent adolescents in crisis. Because the environment centered on neurodivergent youth, Bob chose to disclose that he was autistic. The response from a supervisor was deeply unsettling. He was told that people would be taken aback by him being autistic and that he should refrain from disclosing."),
    bq("I thought that was really unjust."),
    h2("Resilience, Recovery, and Finding the Right Fit"),
    p("One week after being terminated, Bob interviewed with a youth services agency and received a job offer. The contrast was immediate and affirming."),
    bq("It was a very supportive environment. I loved the managers I worked with, the supervisors and the youths there, the co-workers, everyone was great."),
    h2("Practicing Therapy Through Empathy and Strengths"),
    p("Today, Bob works as an outpatient therapist. Being neurodivergent shapes how he engages in therapy. He views it as a lens that allows him to approach situations from a different perspective."),
    bq("When I work with clients, I like to identify what their strengths are, and they can be used as skills to help them reach their goals in treatment."),
    h2("What a Neuro-Affirming Workplace Looks Like"),
    bq("A place that&rsquo;s accepting of neurodivergent individuals and accepting of the ideas that they have."),
    p("Follow Bob on Instagram at @vintage_bob_1989 or connect with him on <a href='https://www.linkedin.com/in/robert-schmus---msw-lcsw-643a07166'>LinkedIn</a>."),
])
fr = make_fr_body(FR_TEXTS["Robert Schmus"])
stories.append(("meeting-people-where-they-are-roberts-journey-as-a-neurodivergent-therapist",
    "Meeting People Where They Are: Robert&rsquo;s Journey as a Neurodivergent Therapist",
    "Autism &middot; ADHD",
    '<img src="/stories/photos/Robert Schmus.jpeg" alt="Robert Schmus" style="object-position: center center;" />',
    en, fr))

# 16 SYDNEY ELAINE BUTLER
en = "\n      ".join([
    p("When Sydney Elaine Butler was six years old, they were diagnosed with autism. At the time, they did not understand what that meant, only that certain things in life felt harder for them than for others. Years later, at 21, they also received a diagnosis of complex post-traumatic stress disorder (CPTSD)."),
    bq("I remember being so excited to take my camera everywhere."),
    h2("Discovering Inclusion in the Workplace"),
    p("At 18, Sydney began working in the inclusion department of a local recreation center, where they supported children, teens, and adults with disabilities."),
    bq("I was masking. I didn&rsquo;t know how much it was impacting me because I was so used to masking my traits. And then when I was working with these individuals, everything was making more sense."),
    p("But when Sydney advocated for more adaptive approaches and safer practices for staff, their concerns were dismissed."),
    bq("When I disclosed my diagnosis, it backfired on me. Rumors were spread about me that I was lazy, that I didn&rsquo;t want to do my job anymore."),
    h2("Building Accessible Creates"),
    p("In 2021, Sydney founded Accessible Creates, an HR and Diversity, Equity, Inclusion, and Accessibility (DEIA) consultancy focused on neurodiversity and disability inclusion."),
    bq("I realized that a lot of businesses don&rsquo;t understand. There seems to be that disconnect between lived experience, policies, procedures and the systems in the organizations."),
    h2("Redefining Work and Rest"),
    bq("I feel like it&rsquo;s so easy for us [neurodivergent folks] to go into burnout, but not even realize that we&rsquo;re in burnout. A lot of times we just equate it with being lazy, but it&rsquo;s not laziness. It&rsquo;s us being tired from all the things we go through."),
    h2("A Vision for True Inclusion"),
    bq("I wish they took the time to get to know us as individuals. We have such complex stories, and you don&rsquo;t know everything somebody&rsquo;s dealing with."),
])
fr = make_fr_body(FR_TEXTS["Sydney Elaine Butler"])
stories.append(("living-through-passion-sydneys-journey-toward-authenticity-and-inclusion",
    "Living Through Passion: Sydney&rsquo;s Journey Toward Authenticity and Inclusion",
    "Autism &middot; CPTSD",
    '<img src="/stories/photos/Sydney Elaine Butler.JPG" alt="Sydney Elaine Butler" />',
    en, fr))

# 17 V GARCIA
en = "\n      ".join([
    p("V Garcia has known they were neurodivergent for as long as they can remember. They have never spoken publicly about their specific diagnosis and are intentional about when and how they will share it."),
    bq("If and when I publicly come out with my specific diagnosis, I want it to be me controlling the narrative."),
    h2("Encounters with Discrimination"),
    p("V experienced a deeply harmful situation in one workplace. After a boss learned they were neurodivergent, the environment shifted dramatically. They described it as &ldquo;outright persecution,&rdquo; something continuous that affected their health, reputation, and long-term career."),
    h2("What Makes a Workplace Work"),
    bq("I lead through vulnerability and by creating psychological safety for my teams. When people are receptive to forming connections as teams, seeing where we align, and learning from each other, those tend to be my most successful places because that&rsquo;s where you can really build that sense of community."),
    h2("Rebuilding Community and Reclaiming Space"),
    p("These days, V has devoted themselves to community work and professional development within the disability and neurodivergent community. Their current passion project explores the experiences of autistic and AuDHD leaders who have disclosed their diagnosis at work."),
    bq("In the isolation that followed that experience, I learned that I needed to build a stronger community."),
    h2("Leadership Shaped by Lived Experience"),
    bq("I think for people to grow, they need to understand that their manager sees them and respects them, is willing to listen, and is really invested in their growth too."),
    h2("Living Out Loud"),
    bq("Be yourself in all spaces. I think that for people to do that, they have to be aware that usually there is a cost. And if they&rsquo;re willing to pay the price for it, to accomplish what they hope, then go for it. Be who you needed when you were younger."),
])
fr = make_fr_body(FR_TEXTS["V Garcia"])
stories.append(("vs-path-to-leadership-courage-community-and-change",
    "V&rsquo;s Path to Leadership: Courage, Community, and Change",
    "Neurodivergent",
    '<img src="/stories/photos/V Garcia.png" alt="V Garcia" />',
    en, fr))

# Write all files
for slug, title, tags, photo_html, body_en, body_fr in stories:
    path = os.path.join(BASE, slug, "index.html")
    content = page(slug, title, tags, photo_html, body_en, body_fr)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {slug}/index.html")

print("\nAll story pages written.")
