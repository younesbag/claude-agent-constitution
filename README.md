<div dir="rtl">

# دستور الوكيل

**عشرة مبادئ تجعل ملفات التعليمات (`CLAUDE.md` و`AGENTS.md` وقواعد `.claude/rules`) ترفع أداء وكلاء Claude بدل أن تربكهم، ونصٌّ جاهز تلصقه في وكيلك فيراجع ملفاتك ويحدّثها بنفسه، بأمان.** محدَّث لـ Claude Fable 5.1 وOpus 5.5.

**← الصفحة: [younesbag.github.io/claude-agent-constitution](https://younesbag.github.io/claude-agent-constitution/)**

## الاستخدام في دقيقة
1. افتح وكيلك (Claude Code أو غيره) داخل مجلد مشروعك.
2. الصق النص الجاهز كاملاً: [العربية](prompt/ar.md) أو [English](prompt/en.md).
3. راجع التقرير والتعديلات المقترحة، واقبل ما تقتنع به. **لا يغيّر الوكيل شيئاً قبل موافقتك.** وحين توافق، يأخذ نسخة احتياطية من كل ملف، وينقل المحتوى حرفياً، ثم يتحقق آلياً من أن شيئاً لم يضِع.

## المواد العشر باختصار
1. **اكتب دليل تشغيل، لا موسوعة.** أقل من ٢٠٠ سطر، وفيه فقط ما لا يُعرف من قراءة الكود.
2. **مع كل قاعدة «لأن».** النماذج الحديثة تعمّم من السبب.
3. **تكلّم بصوت عادي.** CRITICAL وMUST بالأحرف الكبيرة تدفع النماذج الحالية إلى الإفراط.
4. **أعطه الهدف والقيود، لا الخطوات.** عمق التفكير يُضبط بإعداد `effort` لا بـ«فكّر خطوة بخطوة».
5. **لا أرقام من الذاكرة.** جدول «مصدر الحقيقة» يقول من أين تُحسب كل معلومة متغيرة.
6. **«تم» تحتاج دليلاً.** طريقة تحقق حقيقية، ومطابقة كل ادعاء بنتيجة أداة.
7. **كل خطأ دفعت ثمنه يصير سطراً**، والقاعدة الخاطئة تُصلَح في مصدرها.
8. **حدّد متى يسأل، بالضبط.** قائمة تصعيد مغلقة، وسؤال واحد بخيارات وتوصية.
9. **ذاكرة ذرّية تُراجَع.** درس واحد لكل ملف، يُتحقق منه قبل الاعتماد عليه.
10. **النموذج المناسب والجهد المناسب.** حسب صعوبة المهمة لا حجمها، وما يجب دائماً يصير hook.

التفاصيل والأسباب في [الصفحة](https://younesbag.github.io/claude-agent-constitution/).

## المصادر
مبني على توثيق Anthropic الرسمي (توجيه Fable 5.1 وOpus 5.5، وإعداد الجهد، وأفضل ممارسات Claude Code ونظام ذاكرته)، وعلى دروس تكررت في تطبيقه على مشاريع حقيقية. الروابط في الصفحة، وآخر تحقق منها في ٢٤ سبتمبر ٢٠٢٦.

</div>

---

## Agent Constitution (English)

**Ten principles that make your instruction files (`CLAUDE.md`, `AGENTS.md`, `.claude/rules`) improve Claude agents instead of confusing them, plus a ready-made prompt you paste into your agent so it audits and updates those files itself, safely.** Updated for Claude Fable 5.1 and Opus 5.5.

- **Page (Arabic):** https://younesbag.github.io/claude-agent-constitution/
- **Prompt (English):** [prompt/en.md](prompt/en.md). Paste it into Claude Code inside your project. It inventories your instruction files, audits them against the principles, and proposes changes. **It changes nothing until you approve.** When you approve, it backs up each file, moves content verbatim, and checks with a script that nothing was lost.

## Repository layout

| Path | Purpose |
|---|---|
| `prompt/ar.md`, `prompt/en.md` | The ready-made prompt, the single source of truth for its text |
| `src/index.template.html` | Page template |
| `build.py` | Injects the prompt files into the page; `--check` fails if they have drifted apart |
| `index.html` | Built page, served by GitHub Pages |
| `tools/og.html` | Source of the social preview image (`assets/og.png`) |

Edit a prompt file, then run `python build.py`. CI runs `python build.py --check` on every push.

## License and disclaimer

Content is licensed under [CC BY 4.0](LICENSE): copy, adapt, and share it with attribution. This is an **unofficial community framework** with no affiliation to Anthropic. Claude, Fable, Opus, and Sonnet are trademarks of Anthropic.
