# Study-by-study evidence appraisal

Checked on 25 October 2026. The 18 records come from the course bibliography; this is a targeted reconstruction and source audit, not a newly exhaustive systematic search. Twelve records have targeted primary full-text sections checked; four have abstract-level or abstract-plus-slides checks; two have bibliographic checks only. A section check does not mean every appendix or raw dataset was audited. The [register](../evidence/studies.csv) exposes these distinctions in machine-readable form.

## How to interpret the evidence

`direct` concerns developers/programming; `direct-adjacent` concerns systems analysis; `mixed` combines programming and other computer tasks; `indirect` concerns other cognitive/learning tasks; `context` has no music comparison. Access level is separate from relevance or methodological strength.

M11/M12 share a dataset. M10 extends M09 and adds evaluations. Treat these as related research families, not four independent demonstrations of a coding benefit. M13 has an author-name correction, checked separately; its conclusion still lacks a silence baseline.

## M01 — Makayla Moster (2022)

**In the Zone: An Analysis of the Music Practices of Remote Software Developers**. [Primary source](https://github.com/makayla-moster/pdfs/blob/master/papers/2022_ESEM_NewIdea_Paper.pdf) · [DOI](https://doi.org/10.1145/3544902.3546638).

- **Scope / access:** direct / full-text-sections.
- **Population:** Remote developers; methods report 130 collected and 93 retained responses.
- **Design:** Survey of music practices.
- **Finding:** Respondents describe perceived productivity and environmental benefits.
- **Appraisal:** Self-selection and self-report; no controlled code-performance comparison.
- **Locator:** Methods 3.2; discussion 5; limitations 5.4; conclusion 6.

## M02 — Ananga Thapaliya (2021)

**Effect on Brain Activity while Programming with (without) Music**. [Primary source](https://doi.org/10.1109/ICSE-Companion52605.2021.00044) · [DOI](https://doi.org/10.1109/ICSE-Companion52605.2021.00044).

- **Scope / access:** direct / metadata-only.
- **Population:** Not extracted from primary full text.
- **Design:** Programming and brain-activity study; design details not verified.
- **Finding:** No result extracted in this edition.
- **Appraisal:** Primary full text unavailable in this check; metadata is not outcome evidence.
- **Locator:** Publisher-deposited Crossref title and author; conference entry.

## M03 — Laura Barton (2020)

**The Sound of Software Development: Music Listening Among Software Engineers**. [Primary source](https://www.ifi.uzh.ch/en/hasel/people/fritz/publications.html) · [DOI](https://doi.org/10.1109/MS.2019.2906312).

- **Scope / access:** direct / metadata-only.
- **Population:** Not independently extracted from primary full text.
- **Design:** Workplace software-engineer music study.
- **Finding:** No quantitative result extracted in this edition.
- **Appraisal:** Primary full text unavailable in this check; do not infer a causal productivity effect.
- **Locator:** Author institutional publication list; publisher-deposited Crossref metadata.

## M04 — Rustam Ikramov (2019)

**Initial evaluation of the brain activity under different software development situations**. [Primary source](https://ksiresearch.org/seke/seke19paper/seke19paper_215.pdf) · [DOI](https://doi.org/10.18293/SEKE2019-215).

- **Scope / access:** direct / full-text-sections.
- **Population:** Tiny undergraduate music pilots; correlation table shows two participants.
- **Design:** Exploratory EEG during programming with and without music; separate pair-programming experiments.
- **Finding:** Music analyses were inconclusive; no significant music result claimed in the conclusion.
- **Appraisal:** Very small music samples; lost/noisy EEG data; inconsistent counts across sections.
- **Locator:** Table I; section IV; Table V; sections V and VII.

## M05 — André N. Meyer (2017)

**The work life of developers: Activities, switches and perceived productivity**. [Primary source](https://thomas-zimmermann.com/publications/files/meyer-tse-2018.pdf) · [DOI](https://doi.org/10.1109/TSE.2017.2656886).

- **Scope / access:** context / full-text-sections.
- **Population:** 20 professional developers in four companies; average 11 workdays.
- **Design:** In-situ activity monitoring and perceived-productivity observations.
- **Finding:** Developer activity is fragmented and perceived productivity depends on the individual.
- **Appraisal:** No music intervention or music-versus-silence comparison.
- **Locator:** Abstract; study design; results and discussion.

## M06 — Gloria Mark (2008)

**The Cost of Interrupted Work: More Speed and Stress**. [Primary source](https://www.ics.uci.edu/~gmark/chi08-mark.pdf) · [DOI](https://doi.org/10.1145/1357054.1357072).

- **Scope / access:** context / full-text-sections.
- **Population:** Participants in a simulated office email task; sample count not re-extracted.
- **Design:** Laboratory comparison of interrupted and uninterrupted office work.
- **Finding:** Interrupted tasks were faster without a quality difference; stress and effort increased.
- **Appraisal:** Office interruption study; not evidence that background music helps or harms coding.
- **Locator:** Abstract; experimental task and interruptions sections in author-hosted paper.

## M07 — Teresa Lesiuk (2011)

**The Effect of Music Listening, Personality, and Prior Knowledge on Mood and Work Performance of Systems Analysts**. [Primary source](https://scholarship.miami.edu/esploro/outputs/journalArticle/The-Effect-of-Music-Listening-Personality/991031577317402976) · [DOI](https://doi.org/10.4018/jhcitp.2011070105).

- **Scope / access:** direct-adjacent / abstract-only.
- **Population:** 62 systems analysts.
- **Design:** Music-listening treatment before a data-modeling task; 10 minutes.
- **Finding:** Abstract reports mood effects without an apparent effect on model quality.
- **Appraisal:** Institutional abstract only; task is systems analysis; full methods and uncertainty not extracted.
- **Locator:** Institutional abstract; publisher-deposited abstract.

## M08 — Makoto Fukumoto (2024)

**A Feedback Method Adjusting Music Volume Based on User’s Task Performance on Calculation**. [Primary source](https://link.springer.com/chapter/10.1007/978-3-031-71115-2_11) · [DOI](https://doi.org/10.1007/978-3-031-71115-2_11).

- **Scope / access:** indirect / abstract-only.
- **Population:** Sample size not stated in the inspected abstract.
- **Design:** Feedback-adjusted versus fixed music volume during calculation tasks.
- **Finding:** Abstract reports condition differences for three-digit calculation time and volume.
- **Appraisal:** Calculation task; publisher abstract only; not an optimal universal coding-volume rule.
- **Locator:** Publisher abstract; CISIM 2024 pages 154–165.

## M09 — Hiromu Yakura; Tomoyasu Nakano; Masataka Goto (2018)

**FocusMusicRecommender: A System for Recommending Music to Listen to While Working**. [Primary source](https://staff.aist.go.jp/m.goto/PAPER/IUI2018yakura.pdf) · [DOI](https://doi.org/10.1145/3172944.3172981).

- **Scope / access:** mixed / full-text-sections.
- **Population:** Eight students performing ordinary computer work; includes programming and document work.
- **Design:** Recommender evaluation using behavioral concentration estimates and song feedback.
- **Finding:** System evaluation supports preference selection and reduced interaction; no measured code-quality gain.
- **Appraisal:** Small selected sample and proxy outcomes; related journal extension M10.
- **Locator:** Collection of User Data for Evaluation; User Study; Conclusion.

## M10 — Hiromu Yakura; Tomoyasu Nakano; Masataka Goto (2022)

**An automated system recommending background music to listen to while working**. [Primary source](https://link.springer.com/article/10.1007/s11257-022-09325-y) · [DOI](https://doi.org/10.1007/s11257-022-09325-y).

- **Scope / access:** mixed / full-text-sections.
- **Population:** Eight students: four programming and four document writing; additional 25-person interface evaluation.
- **Design:** Extended recommender evaluation; user study and separate crowd-worker interface study.
- **Finding:** Evaluates preference estimation and playback interaction; authors request direct concentration-effect evaluation.
- **Appraisal:** Extends M09 with additional evidence; not wholly independent; coding correctness not measured.
- **Locator:** Introduction; sections 5.1.2 and 5.4; sections 6 and 7.

## M11 — Luca Kiss; Karina J. Linnell (2021)

**The effect of preferred background music on task-focus in sustained attention**. [Primary source](https://link.springer.com/article/10.1007/s00426-020-01400-6) · [DOI](https://doi.org/10.1007/s00426-020-01400-6).

- **Scope / access:** indirect / full-text-sections.
- **Population:** 40 students.
- **Design:** Counterbalanced sustained-attention task with preferred music versus silence.
- **Finding:** Reported task focus increased; mean reaction time and variability did not significantly improve.
- **Appraisal:** Non-coding task; reported focus and measured performance differ.
- **Locator:** Abstract; Methods: Participants and Design; Results.

## M12 — Luca Kiss (2024)

**Music in the eye of the beholder: a pupillometric study on preferred background music, attentional state, and arousal**. [Primary source](https://link.springer.com/article/10.1007/s00426-024-01963-8) · [DOI](https://doi.org/10.1007/s00426-024-01963-8).

- **Scope / access:** indirect / full-text-sections.
- **Population:** 39 students in pupil-based analysis of the M11 dataset.
- **Design:** Pupillometric analysis of preferred music; attentional state and arousal.
- **Finding:** Examines music and pupil-linked arousal using the earlier attention dataset.
- **Appraisal:** Reanalysis of M11; not an independent replication or programming experiment.
- **Locator:** Abstract; Introduction same-dataset statement; Methods.

## M13 — Lena Maria Hofbauer (2024)

**Background music varying in tempo and emotional valence differentially affects cognitive task performance: experimental within-participant comparison**. [Primary source](https://link.springer.com/article/10.1007/s41809-024-00144-8) · [DOI](https://doi.org/10.1007/s41809-024-00144-8).

- **Scope / access:** indirect / full-text-sections.
- **Population:** 40 participants.
- **Design:** Within-participant comparison of two tempi by two emotional valences during cognitive tasks.
- **Finding:** Fast tempo and positive valence helped some outcomes relative to other music conditions.
- **Appraisal:** No silence baseline; one stimulus per cell; cannot establish a music-versus-silence benefit.
- **Locator:** Abstract; Methods; Results; Discussion limitations; author-name correction DOI 10.1007/s41809-024-00150-w.

## M14 — Pietro Sarasso (2022)

**Preferred music listening is associated with perceptual learning enhancement at the expense of self-focused attention**. [Primary source](https://link.springer.com/article/10.3758/s13423-022-02127-8) · [DOI](https://doi.org/10.3758/s13423-022-02127-8).

- **Scope / access:** indirect / full-text-sections.
- **Population:** 18 participants in EEG experiment; separate heartbeat-detection experiment.
- **Design:** Music listening followed by auditory perceptual-learning measures; separate self-focus task.
- **Finding:** Preferred music associated with enhanced perceptual learning and reduced self-focused attention.
- **Appraisal:** Music-before-task and perceptual measures differ from background music during programming.
- **Locator:** Experiment 1: Methods and Procedures; Experiment 2; Discussion.

## M15 — Fanjie Li (2021)

**Studying with Learners’ Own Music: Preliminary Findings on Concentration and Task Load**. [Primary source](https://hub.hku.hk/handle/10722/304830) · [DOI](https://doi.org/10.1145/3448139.3448206).

- **Scope / access:** indirect / abstract-and-slides.
- **Population:** Author slides report seven participants and 28 sessions over three days.
- **Design:** Naturalistic learning sessions with self-selected music; self-reported task load.
- **Finding:** Preliminary learning/concentration patterns varied with task demand.
- **Appraisal:** Institutional abstract and author presentation only; no verified causal coding-performance effect.
- **Locator:** Institutional abstract; author presentation Preliminary Results.

## M16 — Ying Que (2020)

**Exploring the Effect of Personalized Background Music on Reading Comprehension**. [Primary source](https://hub.hku.hk/handle/10722/288290) · [DOI](https://doi.org/10.1145/3383583.3398543).

- **Scope / access:** indirect / abstract-only.
- **Population:** 100 university students reading nine academic passages.
- **Design:** Random allocation to own-choice background music or no music.
- **Finding:** Institutional abstract reports positive emotion maintenance with no reading-performance cost.
- **Appraisal:** Abstract-level appraisal; absence of a detected cost does not prove equivalence or coding benefit.
- **Locator:** Institutional abstract; JCDL 2020 pages 57–66.

## M17 — Fanjie Li (2020)

**Learning with Background Music: A Field Experiment**. [Primary source](https://fanjie-li.netlify.app/media/LAK20/paper_270.pdf) · [DOI](https://doi.org/10.1145/3375462.3375529).

- **Scope / access:** indirect / full-text-sections.
- **Population:** 30 participants studying in their own locations for one week.
- **Design:** Naturalistic mobile-app field study; music-feature correlations.
- **Finding:** Music characteristics related to engagement and perceived performance.
- **Appraisal:** Self-reported learning outcomes; small culturally narrow sample; no coding experiment.
- **Locator:** Abstract; sections 3–5; limitations.

## M18 — Xiao Hu (2019)

**Can Background Music Facilitate Learning? Preliminary Results on Reading Comprehension**. [Primary source](https://fanjie-li.netlify.app/media/LAK19/p101-hu.pdf) · [DOI](https://doi.org/10.1145/3303772.3303839).

- **Scope / access:** indirect / full-text-sections.
- **Population:** 33 graduate students.
- **Design:** Reading under four music conditions and environmental sound.
- **Finding:** No significant overall condition differences in accuracy or reading/answering time; engagement differed.
- **Appraisal:** No silence baseline among the five audio conditions; non-coding task.
- **Locator:** Methods; sections 4.2 and 4.3; Summary.

## Access still needed for a full-text appraisal

M02 and M03 have verified bibliographic identities, but no primary full-text result extraction here. M07, M08 and M16 are abstract-level checks; M15 also has an author-hosted presentation. Obtaining lawful author copies or institutional access would allow deeper checks of exclusions, condition assignment, effect uncertainty and reporting. These access gaps are not filled using unsupported numbers or assumed findings.

The author presentation for M15 is available [here](https://fanjie-li.netlify.app/media/LAK21/slide.pdf). The author-name correction for M13 is [published separately](https://doi.org/10.1007/s41809-024-00150-w). Article PDFs, participant quotations and publisher graphics are not redistributed.

## Review follow-up

M03 remains metadata-only in this edition. Its full-text appraisal has not been completed, so it is not used as verified causal evidence of productivity gains. No new scientific findings are inferred from metadata.
