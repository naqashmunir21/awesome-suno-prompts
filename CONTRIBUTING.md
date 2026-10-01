# Contributing to Awesome Suno Prompts

Thank you for your interest in contributing! This repository thrives on community contributions.

## 🎯 Ways to Contribute

### 1. Add New Prompts
Share prompts that have worked well for you.

### 2. Improve Existing Prompts
Enhance descriptions, add use cases, or suggest optimizations.

### 3. Report Issues
Found a prompt that doesn't work as expected? Let us know!

### 4. Share Success Stories
Generated an amazing song using our prompts? Share it in [examples/](examples/)!

---

## 📝 Prompt Submission Guidelines

### Quality Standards

Your prompt MUST:
- ✅ Produce professional-quality output
- ✅ Be tested on the Suno v6 family (v6, v6-wild, or v6-mini) — all pre-v6 models were retired in September 2026
- ✅ Be tested with **Variety set to 0** (otherwise v6 rewrites your style tags)
- ✅ Include specific production details
- ✅ Stay under 950 characters
- ✅ Avoid generic descriptions

### Format

Use this template when adding prompts:

````markdown
#### [Descriptive Prompt Name]
```
[Your prompt text here - specific instrumentation, vocals, 
production details, BPM, key, etc.]
```
**Use Case:** [When/why to use this prompt]
**Suno Version:** [v6, v6-wild, or v6-mini]
**Energy:** [1-10 scale]
**Notable Feature:** [Optional: What makes this prompt special]
**Example Song:** [Optional: Link to song created with this prompt]
````

**Which model should your prompt target?**
- **v6** — precise, polished results; the default for most prompts
- **v6-wild** — experimental fusions and genre-bending prompts
- **v6-mini** — quick drafts; only tag mini if the prompt is specifically optimized for it

---

## 🔀 Submission Process

### For New Prompts

1. **Fork the repository**
2. **Choose the right file:**
   - Pop → `prompts/pop.md`
   - Rock → `prompts/rock.md`
   - Hip-Hop → `prompts/hip-hop.md`
   - Country → `prompts/country.md`
   - EDM → `prompts/edm.md`
   - R&B/Soul → `prompts/rnb-soul.md`
   - Indie → `prompts/indie.md`
   - Jazz/Blues → `prompts/jazz-blues.md`
3. **Add your prompt** following the format above
4. **Test thoroughly** on Suno before submitting
5. **Submit a Pull Request** with clear description

### For Issue Reports

Use our [issue templates](../.github/ISSUE_TEMPLATE/):
- **Bug Report:** Prompt doesn't work as described
- **Prompt Request:** Request a specific type of prompt
- **Improvement:** Suggest enhancements

---

## ✅ Checklist Before Submitting

- [ ] Tested prompt on the Suno v6 family
- [ ] Tested with Variety = 0 (tags stay exactly as typed)
- [ ] Followed format template exactly
- [ ] Added to correct genre file
- [ ] Prompt under 950 characters
- [ ] Included use case
- [ ] Specified Suno model (v6, v6-wild, or v6-mini)
- [ ] Proofread for typos
- [ ] No duplicates (check existing prompts first)

---

## 🎨 Writing Great Prompts

### DO:
✅ Be specific: "crunchy distorted guitar" not "guitar"  
✅ Include technical details: BPM, key, production terms  
✅ Specify vocal style: raspy, smooth, powerful, breathy  
✅ Mention production approach: radio-ready, lo-fi, live  
✅ Use arrow notation for evolution: "soft intro → explosive chorus"  
✅ Recommend v6-wild for experimental/fusion prompts

### DON'T:
❌ Be vague: "good song", "nice beat"  
❌ Mix contradictory styles: "lo-fi + stadium production"  
❌ Type slider values into the prompt text ("weirdness 20%") — they do nothing on v6  
❌ Exceed character limit (950 chars)  
❌ Copy prompts from other sources without testing  
❌ Submit AI-generated prompts without verification

---

## 📊 Review Process

1. **Automated checks:** PR must pass format validation
2. **Community review:** Other contributors may test and provide feedback
3. **Maintainer approval:** Final review by repo maintainers
4. **Merge:** Your contribution becomes part of the collection!

**Review time:** Usually 2-5 days for new prompts

---

## 🏆 Recognition

Contributors are listed in:
- README.md acknowledgments section
- Individual prompt credits (optional)
- GitHub contributor graph

Top contributors may receive:
- Shoutouts on [@songaifarm](https://twitter.com/songaifarm) Twitter
- Featured in Song AI Farm newsletter
- Early access to new features

---

## 💬 Questions?

- **General discussion:** [GitHub Discussions](https://github.com/naqashmunir21/awesome-suno-prompts/discussions)
- **Quick questions:** [Open an issue](https://github.com/naqashmunir21/awesome-suno-prompts/issues/new)
- **Direct contact:** hello@songaifarm.com

---

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Provide constructive feedback
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Unacceptable Behavior

- Harassment or discriminatory language
- Trolling or insulting comments
- Spam or promotional content (except in designated areas)
- Publishing others' private information

**Violations:** May result in temporary or permanent ban

---

## 🙏 Thank You!

Every contribution makes this resource better for thousands of musicians worldwide.

**Not ready to contribute yet?**
- ⭐ Star the repository
- 🔀 Share with fellow musicians
- 💬 Join the discussion
- 🎵 Create amazing music with these prompts!

---

**Made with 💚 by the [Song AI Farm](https://www.songaifarm.com) community**
