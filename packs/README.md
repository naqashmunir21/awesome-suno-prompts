# 📦 Awesome Suno Prompts — Downloadable Packs

Free, ready-to-use prompt collections in JSON and Markdown formats. Perfect for importing into Notion, Obsidian, or custom tools.

---

## 📋 Available Packs

| Pack | Prompts | Format | Best For | Download |
|------|---------|--------|----------|----------|
| **Viral TikTok/Reels** | 15 | JSON + MD | Gym edits, dance challenges, 30s loops | [JSON](viral-tiktok-reels.json) · [MD](viral-tiktok-reels.md) |
| **Gym & Workout** | 12 | JSON | Phonk, Corridos Tumbados, Aggressive | [JSON](gym-workout.json) |
| **Heartbreak & Emotional** | 15 | JSON | Sad Sierreño, Melodic Phonk, Ballads | [JSON](heartbreak-emotional.json) |
| **Cross-Genre Fusion** | 10 | JSON | Afro-Phonk, K-Pop Jersey, Corrido Phonk | [JSON](cross-genre-fusion.json) |
| **Complete Starter** | 50 | JSON | All viral genres combined | [JSON](complete-starter.json) |

---

## 🚀 Quick Start

### Download All Packs
```bash
# Clone just the packs folder (shallow clone)
git clone --depth 1 --filter=blob:none --sparse https://github.com/naqashmunir21/awesome-suno-prompts
cd awesome-suno-prompts
git sparse-checkout set packs
```

### Or Download Individual Files
Click the links in the table above.

---

## 📋 JSON Schema

Each prompt object follows this structure:

```json
{
  "id": "unique-identifier",
  "title": "Prompt Display Name",
  "genre": "phonk | afrobeats | k-pop | jersey-club | regional-mexican | pop | rock | hip-hop | country | edm | rnb | indie | jazz-blues",
  "subgenre": "drift-phonk | amapiano | corridos-tumbados | sad-sierreno | etc",
  "prompt": "Full Suno prompt text (under 950 chars)",
  "useCase": "When to use this prompt",
  "sunoVersion": "V4.5 | V5 | Both",
  "energy": 1-10,
  "bpm": 140,
  "key": "D Minor",
  "tags": ["gym", "viral", "30s-loop", "tiktok"],
"source": "README | prompts/phonk.md | community-contribution"
}
```

---

## 🛠️ Usage Examples

### Import into Notion
1. Download the `.json` file
2. In Notion: **Import → JSON** → Select file
3. Creates a database with all fields as properties

### Import into Obsidian
1. Download the `.md` file (or convert JSON to MD)
2. Place in your vault
3. Use Dataview plugin to query:
```dataview
TABLE genre, energy, bpm
FROM "packs"
```

### Use with Python
```python
import json

with open('packs/viral-tiktok-reels.json') as f:
    prompts = json.load(f)

# Random prompt for quick generation
import random
prompt = random.choice(prompts)['prompt']
print(prompt)

# Filter by criteria
gym_phonk = [p for p in prompts if 'gym' in p['tags'] and p['genre'] == 'phonk']
high_energy = [p for p in prompts if p['energy'] >= 8]
```

### Filter with JavaScript
```javascript
const prompts = await fetch('packs/complete-starter.json').then(r => r.json());

// Gym phonk only
const gymPhonk = prompts.filter(p => p.tags.includes('gym') && p.genre === 'phonk');

// High energy (8+)
const highEnergy = prompts.filter(p => p.energy >= 8);

// Specific BPM range
const workoutBPM = prompts.filter(p => p.bpm >= 130 && p.bpm <= 150);
```

---

## 📥 Lead Magnet: Get the "Pro Pack" (Free with Email)

**Want 200+ more prompts** including:
- 50 exclusive viral formulas not in this repo
- Artist-style strings for 100+ 2026 rising stars
- Song structure templates for every genre
- Negative constraint library (what to avoid)
- Monthly updated viral trend prompts

**[📧 Get the Pro Pack Free →](https://www.songaifarm.com/pro-pack)**

*No spam. Unsubscribe anytime. 50,000+ creators already subscribed.*

---

## 🔄 Auto-Update via GitHub Action

Packs are regenerated weekly from the main `prompts/` folder.

**Last updated:** July 2026  
**Next update:** Every Monday via GitHub Action

---

## 🤝 Contribute to Packs

Found a prompt that should be in a pack? 
1. Add it to the appropriate `prompts/*.md` file
2. Open a PR
3. Packs auto-regenerate on merge

---

*Part of the [Awesome Suno Prompts](../README.md) ecosystem — Made with 💚 by [Song AI Farm](https://www.songaifarm.com)*

