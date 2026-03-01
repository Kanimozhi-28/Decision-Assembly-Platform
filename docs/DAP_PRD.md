# Product Requirements Document (PRD)
## Decision Assembly Platform v1.1

**Document Version:** 1.2  
**Last Updated:** February 14, 2026  
**Status:** Updated - Logical UX & Assembly Rules Integrated

---

## Table of Contents

1. [Vision](#1-vision)
2. [Product Overview](#2-product-overview)
3. [Problem Statement](#3-problem-statement)
4. [Target Users](#4-target-users)
5. [Unique Selling Propositions (USPs)](#5-unique-selling-propositions-usps)
6. [Scope](#6-scope)
7. [Functional Requirements](#7-functional-requirements)
   - 7.1 Commentary Strip
   - 7.2 Trigger Detection System
   - 7.2.1 Event Catalog (User Events Used)
   - 7.2.2 Event Buffer and State
   - 7.2.3 Event-to-Trigger Mapping (Formal Rules)
   - 7.2.4 Trigger Priority and Combinatorics
   - 7.2.5 Business and Scoring Logic (Complete)
   - 7.3 Intent Selection
   - 7.4 Grid Assembly
   - 7.5 Rationale Display
   - 7.6 Intent → Block Mapping
   - 7.6.1 Assembly Logic by Intent (Logical UX Rules)
   - 7.6.2 End-to-End User Flow Diagram (Any Product Site)
   - 7.7 Admin Portal
   - 7.7.1 Content & Vector Structure (Multi-Site, Multi-Domain)
   - 7.8 Website Integration
   - 7.9 Decision Canvas Block Interactions
   - 7.10 Empty Blocks (User-Pulled Content)
   - 7.11 Custom Query Block
   - 7.12 Session Management
8. [Non-Functional Requirements](#8-non-functional-requirements)
9. [User Flows](#9-user-flows)
10. [UX Design Details](#10-ux-design-details)
11. [Conclusion](#11-conclusion)

---

## 1. Vision

**To eliminate decision friction on websites by helping users assemble clarity through context-aware information blocks—without conversation.**

The Decision Assembly Platform transforms how users make decisions online. Instead of forcing users to navigate complex websites or engage in lengthy chatbot conversations, the platform intelligently assembles the right information at the right time, making decisions obvious and actions confident.

---

## 2. Product Overview

### 2.1 What It Is

The **Decision Assembly Platform (DAP)** is a website-embedded system that:

- Lives inside existing websites (banking, insurance, SaaS, e-commerce)
- Appears as a **silent virtual guide** (elegant strip at bottom)
- Observes user behavior passively
- Activates only when decision friction is detected
- Assembles relevant products/information in a grid format
- Shows rationale for why each item is recommended

### 2.2 What It Is NOT

- ❌ A chatbot or conversational AI
- ❌ An FAQ assistant
- ❌ A traditional recommendation engine
- ❌ A search tool

### 2.3 Core Philosophy

> **The experience that appears IS the product.**  
> The input box is not the product. Users assemble information until the decision becomes obvious.

---

## 3. Problem Statement

### 3.1 The Core Problem

On websites with multiple products or options, users face significant decision friction:

| Problem | Why It's Major | Impact |
|---------|----------------|--------|
| **Information Overload** | Users are overwhelmed by too many options without clear guidance | High bounce rates, delayed decisions, abandoned carts |
| **Repetitive Navigation** | Users visit the same pages multiple times, unable to compare effectively | Increased time-to-decision, frustration, lower conversion |
| **Chatbot Friction** | Chatbots require users to articulate needs in words, adding cognitive load | Low engagement rates, generic responses, user abandonment |
| **Lack of Context** | Users must manually piece together information from different pages | Decision paralysis, incomplete comparisons, wrong choices |
| **No Transparency** | Users don't understand why certain products are shown or recommended | Low trust, hesitation, missed opportunities |

### 3.2 Root Cause

**Users are forced to figure out decisions themselves instead of being helped to assemble clarity.**

Traditional solutions (chatbots, filters, search) require users to:
- Know what they're looking for
- Articulate their needs
- Navigate complex information hierarchies
- Make decisions without sufficient context

### 3.3 How DAP Solves This

| Solution | How It Works |
|----------|--------------|
| **Passive Observation** | System watches user behavior without requiring input |
| **Intent Confirmation** | User explicitly selects intent (no prediction needed) |
| **Context Assembly** | Relevant products/information assembled automatically |
| **Transparent Rationale** | Clear explanation of why each item is shown |
| **No Conversation** | Structured blocks instead of chat interface |

---

## 4. Target Users

### 4.1 Primary Users (End Users)

| User Type | Characteristics | Use Case |
|-----------|----------------|----------|
| **Decision-Makers** | Evaluating multiple products/options | Need help comparing and choosing |
| **Hesitant Buyers** | Unsure which option fits their needs | Need clarity on differences and fit |
| **Comparison Shoppers** | Actively comparing similar offerings | Need side-by-side information assembly |

### 4.2 Secondary Users (Business Users)

| User Type | Role | Needs |
|-----------|------|-------|
| **Product Managers** | Managing product catalogs | Increase conversion, reduce friction |
| **Marketing Teams** | Driving user engagement | Better user experience, higher engagement |
| **CRO Teams** | Optimizing conversion rates | Reduce bounce rates, increase actions |
| **Enterprise Website Owners** | Managing websites | Zero-code integration, white-label solution |

---

## 5. Unique Selling Propositions (USPs)

### 5.1 Competitive Landscape

| Product Type | Examples | Limitations | DAP Advantage |
|--------------|----------|-------------|---------------|
| **Chatbots** | Intercom, Drift, Zendesk | Require conversation, generic responses | No conversation needed, context-aware assembly |
| **Recommendation Engines** | Amazon Recommendations, Netflix | Black-box algorithms, no rationale | Transparent rationale, user-controlled |
| **Comparison Tools** | Compare.com, G2 | Manual input required, static | Automatic assembly, dynamic grid |
| **Product Filters** | Standard e-commerce filters | User must know what to filter | System suggests based on behavior |

### 5.2 DAP's Unique Differentiators

1. **Experience IS the Product**
   - The assembled grid with rationale is the core value
   - Not a tool, but an experience layer

2. **Silent Virtual Guide**
   - Always-on commentary strip
   - Non-intrusive, elegant, informative

3. **Explicit Intent (Not Predicted)**
   - User selects intent explicitly
   - No ML-based prediction (v1)
   - Transparent and controllable

4. **Transparent Rationale**
   - Every recommendation shows "Why this?"
   - Builds trust and confidence

5. **Zero-Conversation Approach**
   - Structured blocks, not chat
   - Reduces cognitive load

6. **Zero-Code Integration**
   - Two lines of JavaScript
   - No backend changes required

---

## 6. Scope

### 6.1 In-Scope (v1)

| Category | Features |
|----------|----------|
| **Core Experience** | Commentary strip, intent selection, grid assembly, rationale display |
| **Trigger System** | Rule-based triggers (behavioral patterns, explicit clicks), priority system, cooldown periods |
| **Intent Types** | 5 intents (Help me choose, Compare options, Check eligibility, Understand differences, Just exploring) |
| **Block Types** | 12 block types (Product Shortlist, Comparison, Benefits, Costs, Eligibility, etc.) |
| **Block Interactions** | Drag-and-drop reordering, expand/collapse, removal, empty blocks (user-pulled content) |
| **Session Management** | Session boundaries, state persistence, restoration on reload |
| **Error Handling** | Empty results handling, Vector DB failure fallbacks, query timeouts |
| **Admin Portal** | Website onboarding, vector content management, trigger configuration, white-labeling, product page config |
| **Integration** | JavaScript SDK, zero-code installation |

### 6.2 Out-of-Scope (v1)

| Category | Features (Future Consideration) |
|----------|----------------------------------|
| **ML-Based Features** | Advanced behavioral ML, intent prediction, personalization |
| **Conversational** | Chatbot fallback, conversational AI |
| **Cross-Session** | Cross-session personalization, user accounts |
| **Advanced Features** | Human advisor workflows, cross-site learning |

---

## 7. Functional Requirements

### 7.1 Commentary Strip (Always-On Layer)

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-001** | **Strip Display** | Fixed bottom strip (40-50px height), always visible | Renders on page load, persists across navigation | Must |
| **FR-002** | **Real-Time Commentary** | Shows English text describing user behavior | Updates based on event listeners (scroll, click, hover, time) | Must |
| **FR-003** | **Commentary Examples** | Dynamic text based on user actions | Template-based: "You've viewed 3 credit cards in 2 minutes" | Must |
| **FR-004** | **Non-Intrusive Design** | Minimal, elegant, readable | CSS positioning, auto-updates, <5ms latency | Must |

**Business Logic:**
- Event listeners track: page views, product views, time spent, hover events, navigation patterns
- Commentary updates trigger on: new page view, product view threshold, time milestones, hover events
- Text templates map to behavior patterns (configurable in admin)
- **Update Throttling:** Debounce commentary updates (500ms) to prevent rapid changes
- **Batching:** Batch rapid events into single update (max 1 update per 2 seconds)
- **Mobile Positioning:** Use `safe-area-inset-bottom` CSS to avoid mobile browser UI overlap

**SDK configuration (clinical logic):**
- **CTA selector:** Admin configures which DOM elements count as "CTA" for hover (e.g. `cta_selectors: [".btn-apply", "[data-cta]"]`). SDK attaches hover listeners only to these; other clicks/hovers do not increment CTA hover count.
- **"Help me choose" selector:** Admin may configure an in-page button selector (e.g. `help_me_choose_selector: "[data-dap-help]"`). When user clicks that element, SDK treats it as **explicit trigger** (immediate intent menu) and does not require other behavioral rules.
- **Product ID source:** Admin configures how SDK derives `product_id` for "products viewed" and for assemble context: e.g. from URL path segment, from `[data-product-id]` (or configurable attribute), or from a meta tag. Same source is used consistently for event buffer and for `context.product_ids` sent to assemble.

---

### 7.2 Trigger Detection System

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-005** | **Behavioral Pattern Triggers** | Detect decision friction patterns | Rule-based if-then logic | Must |
| **FR-006** | **Multiple Product Views** | Trigger when user views 2+ products in 5 minutes | `IF (distinct_products_viewed >= 2) AND (time_window <= 5_min) → TRIGGER` | Must |
| **FR-007** | **Hesitation Detection** | Trigger on long dwell without action | `IF (page_dwell >= 45s) AND (no_cta_click) AND (scroll_depth > 60%) → TRIGGER` | Must |
| **FR-008** | **CTA Hover Pattern** | Trigger on CTA hover without click | `IF (cta_hover_count >= 2) AND (no_click) AND (dwell > 30s) → TRIGGER` | Must |
| **FR-009** | **Navigation Loops** | Trigger on repeated page visits | `IF (same_page_revisit >= 2) AND (time_between < 3_min) → TRIGGER` | Must |
| **FR-010** | **Explicit User Trigger** | Manual "Help me choose" button click | `IF (user_clicks_button) → IMMEDIATE_TRIGGER` | Must |
| **FR-010A** | **Product Page Validation** | Only trigger on configured product pages | `IF (page_is_product_page) AND (trigger_condition) → TRIGGER` | Must |
| **FR-010B** | **Trigger Priority System** | Resolve conflicts when multiple triggers fire | Priority: Explicit > Multiple Products > CTA Hover > Hesitation > Loops | Must |
| **FR-010C** | **Trigger Cooldown** | Prevent trigger spam | Cooldown: 30s after trigger, 60s after dismiss, 45s after grid close | Must |
| **FR-010D** | **Dismissal Tracking** | Track user dismissals to suppress triggers | If dismiss 2+ times → Suppress triggers for session | Should |

**Business Logic:**
- Event counting: Track distinct products, page visits, hover events, time windows
- Threshold-based: Configurable thresholds in admin (defaults: 2 products, 5 min window, 45s dwell)
- Deterministic: No ML, pure rule-based logic
- Performance: <50ms trigger detection latency
- **Product Page Detection:** Admin configures product URL patterns (e.g., `/products/*`, `/cards/*`) or DOM selectors
- **Trigger Priority:** When multiple triggers fire simultaneously, use highest priority trigger only
- **Cooldown Logic:** 
  - After trigger fires: 30-second cooldown
  - After user dismisses intent menu: 60-second cooldown
  - After user selects intent: No cooldown (user engaged)
  - After grid closes: 45-second cooldown
- **Dismissal Suppression:** Track dismissals (X button, click outside), suppress triggers if 2+ dismissals in session
- **Event buffer reset on session timeout:** When session times out (e.g. 30 min idle per FR-052), SDK MUST clear the event buffer (product views, dwell, CTA hovers, same-page revisit counts) so trigger rules re-evaluate from scratch on next activity.
- **Page title in context:** SDK MUST include current page title in the context sent to assemble (e.g. from `document.title` or from an admin-configured selector). Used by RAG to improve query relevance.

#### 7.2.1 Event Catalog (User Events Used)

All user events that feed the trigger system and commentary are listed below. **Intent is never inferred from events;** the user always selects intent from the 5 options after a trigger fires. Events only determine **whether** the strip CTA is shown (trigger fired) and **what** commentary text is displayed.

| Event ID | Event name | When recorded | What it updates in event buffer | Used by trigger(s) |
|----------|------------|----------------|----------------------------------|---------------------|
| E1 | **page_view** | Navigation (URL change, history/popstate, SPA route change) | current_url, page_load_ts; resets dwell for new page; may increment same_page_revisit for same URL | Hesitation, Loops, Commentary |
| E2 | **product_view** | Same as page_view but only when current URL/DOM matches product_page_rules | distinct_product_ids (add product_id), product_view_timestamps (per product_id or first/last in window) | Multiple Product Views, Commentary |
| E3 | **dwell_update** | Timer (e.g. every 1s or on visibility change) while user is on page | current_page_dwell_sec, last_activity_ts | Hesitation, CTA Hover (min dwell), Commentary |
| E4 | **scroll_depth** | On scroll: max scroll percentage seen | scroll_depth_pct (0–100) | Hesitation |
| E5 | **cta_hover** | Mouse enter on element matching cta_selectors from config | cta_hover_count (incremented once per enter per session or per page per config) | CTA Hover Pattern |
| E6 | **cta_click** | Click on element matching cta_selectors | cta_clicked = true (or resets CTA-hover-based trigger for current page) | Disables Hesitation and CTA Hover (no_click condition) |
| E7 | **same_page_revisit** | page_view where URL equals a URL already visited in session within the configured window | same_page_revisit_count, last_revisit_ts per URL (or global max) | Navigation Loops |
| E8 | **explicit_help_click** | Click on element matching help_me_choose_selector (or strip click when strip is the only “explicit” path if selector unset) | N/A (immediate trigger) | Explicit User Trigger |

**Note:** Strip click (user clicks the commentary strip) is not an “event” that updates the buffer; it is the **action** that opens the intent picker after a trigger has already fired. The **explicit trigger** is either (1) click on help_me_choose_selector, or (2) in implementations where strip can open intent without a prior behavioral trigger, strip click may be treated as “user asked for help” (same outcome: intent picker opens).

#### 7.2.2 Event Buffer and State

The SDK maintains the following **event buffer** (in-memory, keyed by session). All values are reset on session timeout (FR-052) or when session is cleared.

| Buffer variable | Type | Description | Config / default |
|-----------------|------|-------------|-------------------|
| distinct_product_ids | Set of string | Product IDs from pages that matched product_page_rules | — |
| product_first_ts | Timestamp | Time of first product view in current “window” | — |
| product_last_ts | Timestamp | Time of most recent product view | — |
| current_page_dwell_sec | Number | Seconds on current page (since last page_view) | — |
| scroll_depth_pct | Number 0–100 | Maximum scroll depth on current page | — |
| cta_hover_count | Integer | Count of CTA hover events (on cta_selectors) in session or per page per config | — |
| cta_clicked | Boolean | True if user clicked a CTA on current page (resets on page_view) | — |
| same_page_revisit_count | Integer | For current URL: number of revisits in window | — |
| same_page_last_visit_ts | Timestamp | Last time we saw this URL (for revisit window) | — |
| last_activity_ts | Timestamp | Last time any event was recorded (for session timeout) | — |
| dismissal_count | Integer | Number of times user dismissed intent menu this session | Default 0; max 2 then suppress |
| cooldown_until_ts | Timestamp | Do not fire trigger before this time | Set by cooldown rules |
| current_url | String | Current page URL | — |

**Product page check:** Before incrementing product_view or distinct_product_ids, SDK checks current URL (and optionally DOM) against product_page_rules (url_patterns, dom_selectors). Only then is product_id derived (from product_id_source) and added to distinct_product_ids.

#### 7.2.3 Event-to-Trigger Mapping (Formal Rules)

Each trigger is a **boolean condition** on the event buffer and config thresholds. When evaluated (e.g. on every relevant event or on a short timer), if the condition is true, that trigger is **candidate** to fire. Cooldown and dismissal checks then decide if the strip CTA is shown.

| Trigger | Priority (order) | Formal condition (all must be true) | Config keys (defaults) |
|---------|------------------|--------------------------------------|-------------------------|
| **Explicit** | 1 (highest) | User clicked element matching help_me_choose_selector (or strip click if that is the explicit path). No other conditions. | help_me_choose_selector |
| **Multiple Product Views** | 2 | distinct_product_ids.size >= multi_product_min AND (now - product_first_ts) <= multi_product_window_min * 60 (seconds). Product views are only counted on pages matching product_page_rules. | multi_product_min (2), multi_product_window_min (5) |
| **CTA Hover Pattern** | 3 | cta_hover_count >= cta_hover_min AND current_page_dwell_sec >= cta_hover_min_dwell_sec AND cta_clicked === false | cta_hover_min (2), cta_hover_min_dwell_sec (30) |
| **Hesitation** | 4 | current_page_dwell_sec >= dwell_sec AND scroll_depth_pct >= scroll_depth_min_pct AND cta_clicked === false | dwell_sec (45), scroll_depth_min_pct (60) |
| **Navigation Loops** | 5 (lowest) | same_page_revisit_count >= same_page_revisit_min AND (now - same_page_last_visit_ts) <= same_page_revisit_window_min * 60 | same_page_revisit_min (2), same_page_revisit_window_min (3) |

**Product page requirement (FR-010A):** For **Multiple Product Views**, the count only includes pages that match product_page_rules (so distinct_product_ids only contains IDs from product pages). For **Hesitation**, **CTA Hover**, and **Navigation Loops**, the trigger is evaluated on the current page (any URL); no requirement that the page be a “product page.”

**Cooldown and dismissal (gating):** Before showing the strip CTA, SDK MUST also ensure: (1) now >= cooldown_until_ts, and (2) dismissal_count < 2. If either fails, no trigger is shown even if a condition is true.

#### 7.2.4 Trigger Priority and Combinatorics

**Priority order when multiple triggers are true:** Only **one** trigger is used to decide that “we will show the strip CTA.” The **highest-priority** trigger that is true wins. Intent is **not** preselected; the user always sees the same 5 intent options and chooses one.

| Priority rank | Trigger | When it is true (summary) |
|----------------|---------|----------------------------|
| 1 | Explicit | User clicked help_me_choose_selector (or strip as explicit) |
| 2 | Multiple Product Views | ≥2 product pages in window (e.g. 5 min) |
| 3 | CTA Hover | ≥2 CTA hovers, dwell ≥30s, no CTA click |
| 4 | Hesitation | Dwell ≥45s, scroll ≥60%, no CTA click |
| 5 | Navigation Loops | Same page revisited ≥2 times in window (e.g. 3 min) |

**Combinatorics (which sequence of events triggers which):**

- **Explicit:** Single event E8 (explicit_help_click). No sequence; immediate.
- **Multiple Product Views:** Sequence of ≥2 E2 (product_view) events on different product_ids within the time window. Order does not matter; only distinct count and window matter.
- **CTA Hover:** At least 2× E5 (cta_hover), with E3 (dwell_update) showing current_page_dwell_sec ≥ 30, and no E6 (cta_click) on current page.
- **Hesitation:** E3 (dwell_update) ≥ 45s, E4 (scroll_depth) ≥ 60%, and no E6 (cta_click) on current page.
- **Navigation Loops:** At least 2× E1 (page_view) for the **same** URL within the revisit window (e.g. 3 min).

**Combination matrix (multiple triggers true at once):** When more than one trigger condition is true at the same evaluation time, the system does **not** show multiple CTAs or multiple intents. It picks the **single** trigger with the **lowest priority rank number** (Explicit = 1, then Multiple Products = 2, etc.) and uses that only for analytics or optional strip copy tailoring. The user always sees one “Want help? Click here” and one intent picker with 5 options.

| Explicit | Multi-product | CTA Hover | Hesitation | Loops | Winner (strip CTA shown) |
|----------|---------------|-----------|------------|-------|---------------------------|
| ✓ | ✓ | ✓ | ✓ | ✓ | Explicit |
| — | ✓ | ✓ | ✓ | ✓ | Multiple Product Views |
| — | — | ✓ | ✓ | ✓ | CTA Hover |
| — | — | — | ✓ | ✓ | Hesitation |
| — | — | — | — | ✓ | Navigation Loops |

(✓ = condition true; — = not required. Row indicates which combination; winner is the one with highest priority among those true.)

#### 7.2.5 Business and Scoring Logic (Complete)

**Business logic (all rules in one place):**

| Rule | Description | Config / value |
|------|-------------|----------------|
| **Trigger thresholds** | See §7.2.3 table. All numeric thresholds are admin-configurable in trigger_thresholds (site_config). | multi_product_min, multi_product_window_min, dwell_sec, scroll_depth_min_pct, cta_hover_min, cta_hover_min_dwell_sec, same_page_revisit_min, same_page_revisit_window_min |
| **Cooldown after trigger** | From the moment a trigger fires (strip CTA shown), no other trigger may fire for cooldown_after_trigger_sec. | Default 30 s |
| **Cooldown after dismiss** | From the moment user dismisses the intent menu (X or click outside), no trigger may fire for cooldown_after_dismiss_sec. | Default 60 s |
| **Cooldown after grid close** | From the moment user closes the grid, no trigger may fire for cooldown_after_grid_close_sec. | Default 45 s |
| **No cooldown after intent selection** | When user selects an intent and grid is shown, no cooldown is applied for that action; next trigger can fire after its own cooldown when conditions are met. | — |
| **Dismissal suppression** | If user dismisses the intent menu (without selecting an intent) 2 or more times in the session, no further triggers fire for the rest of the session. | dismissal_count >= 2 → suppress |
| **Session timeout** | After session_timeout_min minutes with no activity (no event), session resets: event buffer and dismissal_count cleared; cooldown cleared. | session_timeout_min (default 30) |
| **Product page rules** | Only pages matching product_page_rules (url_patterns and/or dom_selectors) count as “product” for distinct_product_ids and Multiple Product Views trigger. | product_page_rules in site_config |
| **CTA and explicit selectors** | Only elements matching cta_selectors count for cta_hover; only element matching help_me_choose_selector counts for explicit trigger. | cta_selectors, help_me_choose_selector in site_config |
| **Commentary throttling** | Commentary strip text updates at most once per 2 s and debounced by 500 ms. | Hardcoded or config |
| **Trigger evaluation latency** | Trigger evaluation (run rules, pick winner, check cooldown/dismissal) must complete in &lt;50 ms. | NFR |

**Scoring logic:**

- **Intent:** There is **no** scoring or ranking of intents. The user selects one of 5 intents; no algorithm assigns a score to “Help me choose” vs “Compare options.” Intent is **always** user-selected.
- **Trigger “winner”:** When multiple triggers are true, the only “score” is **priority rank** (1–5). The trigger with the smallest rank number wins. No numeric score is computed.
- **RAG/Assembly:** After intent is chosen, the backend uses **vector similarity** (embedding distance) to rank search results. That is assembly/relevance scoring, not intent scoring; see PRD §7.4 and TAD §8.3.

**Default trigger_thresholds (recommended schema):**

```json
{
  "multi_product_min": 2,
  "multi_product_window_min": 5,
  "dwell_sec": 45,
  "scroll_depth_min_pct": 60,
  "cta_hover_min": 2,
  "cta_hover_min_dwell_sec": 30,
  "same_page_revisit_min": 2,
  "same_page_revisit_window_min": 3,
  "cooldown_after_trigger_sec": 30,
  "cooldown_after_dismiss_sec": 60,
  "cooldown_after_grid_close_sec": 45
}
```

---

### 7.3 Intent Selection

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-011** | **Intent Menu Display** | Show intent options when trigger fires | Modal/overlay appears with 5 intent options | Must |
| **FR-012** | **Intent Options** | 5 predefined intents | Help me choose, Compare options, Check eligibility, Understand differences, Just exploring | Must |
| **FR-013** | **Intent Selection** | User clicks to select intent | State management stores selected intent | Must |
| **FR-014** | **Intent Change** | User can change intent anytime | Intent selector remains accessible | Should |
| **FR-015** | **Intent Confirmation** | Explicit confirmation before grid assembly | User must select intent before grid appears | Must |

**Business Logic:**
- Trigger fires → Strip shows: "Looks like you're comparing options. Want help?"
- User clicks → Intent menu appears (overlay/modal)
- User selects → System stores intent, proceeds to grid assembly
- Intent persists until changed or session ends
- **Session Management:** Intent stored in sessionStorage (survives page reload if <5 minutes old)
- **Navigation Behavior:** Intent persists across navigation, but grid closes on navigation
- **Intent Change Logic:** If grid is open and user changes intent → Close grid → Show loading → Rebuild grid with new blocks → Animate transition
- **Restore on Reload:** If page reloads within 5 minutes, restore intent and show "Continue where you left off?" prompt

---

### 7.4 Grid Assembly (Core Experience)

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-016** | **Product Discovery** | Query Vector DB for relevant products | RAG-based semantic search using page context + intent | Must |
| **FR-017** | **Context Extraction** | Extract current page context | Parse URL, DOM content, products viewed in session | Must |
| **FR-018** | **Vector DB Query** | Semantic search for products | Query with intent + context, return top N (default: 3-5) | Must |
| **FR-019** | **Grid Rendering** | Responsive grid (2-3 columns) | React component, lazy loading, responsive design | Must |
| **FR-020** | **Product Cards** | Each card shows key information | Name, features (3-4 bullets), price/cost, eligibility indicator | Must |
| **FR-021** | **Grid Layout** | Adaptive columns based on screen size | 3 columns (desktop), 2 columns (tablet), 1 column (mobile) | Must |

**Business Logic:**
1. Extract context: Page URL, products viewed (`product_ids`), content read, selected intent
2. **Intent-specific product set:** For "Compare options" and "Understand differences" the grid MUST contain only products in `context.product_ids` (see §7.6.1). For other intents, semantic search returns top N.
3. Query Vector DB: For Compare/Understand — filter by `product_id` in `context.product_ids`; for Help me choose / Just exploring — semantic search with context + intent
4. Rank products: Relevance score + intent match + user behavior signals (where applicable)
5. Return top N: Default 3-5 products (configurable); for Compare/Understand, N = size of user's set (capped by config)
6. Render grid: Assemble cards in responsive layout

**Performance:** <100ms for RAG query + grid render

**Error Handling & Edge Cases:**
- **Empty Results:** If Vector DB returns 0 products → Show "No products found matching your criteria" → Offer "Try different intent?" or "Browse all products" → Fallback: Show top 3 products by popularity (if available)
- **Query Timeout:** If query takes >200ms → Show cached results (if <24 hours old) OR skeleton loading state OR progressive loading (show top 3, load rest async)
- **Vector DB Failure:** Try-catch around query → Fallback to cached results OR fallback grid (top products by popularity) → Show: "Having trouble loading — showing popular options"
- **Too Many Products:** If >5 results → Show top 5 → "View 10 more" button → Pagination (5 per page) → "Show all" option (with performance warning)
- **Product Limit:** Default 5 products, pagination for overflow, admin configurable limit

**RAG & fallback (clinical logic):**
- **Definition of "popular" fallback:** When RAG returns 0 products, fallback = top N (e.g. 3) by **most recently indexed** (indexed_at) for that site. Alternative: admin-configured "featured" product IDs. Document as single strategy per deployment (default: recency).
- **Query when only product_ids:** If context has product_ids but no page_title (e.g. SPA or missing title), backend builds query from intent label + product identifiers; may resolve product titles from stored payload for query text. Never send an empty query to the vector search.
- **Payload → block/card mapping:** Backend maps Qdrant payload fields (title, url, price, features, eligibility, product_id) to product card and block structure per intent→block mapping (§7.6). One canonical mapping so all sites produce consistent card shape.
- **Empty block "pull content":** For empty blocks (FR-041–044), SDK sends POST /assemble with same site_id and intent, plus `block_type` or `pull_query` (e.g. "pricing"). Backend runs same RAG path with query scoped to that block type and returns content for that block only (no full grid).

---

### 7.5 Rationale Display

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-022** | **"Why This?" Button** | Clickable button on each product card | Opens rationale panel for that product | Must |
| **FR-023** | **Rationale Panel** | Shows explanation for recommendation | Template-based + context injection | Must |
| **FR-024** | **Rationale Examples** | Context-aware explanations | "You viewed 2 similar products → this matches your comparison pattern" | Must |
| **FR-025** | **Rationale Types** | Different rationale based on intent | Comparison rationale vs. recommendation rationale | Must |

**Business Logic:**
- Template-based: Pre-defined rationale templates
- Context injection: User behavior + intent + product attributes
- Examples:
  - Comparison: "You viewed 2 premium cards → this offers best rewards"
  - Eligibility: "You checked eligibility → you qualify for this"
  - Recommendation: "Based on your browsing → this fits your use case"
- **Rationale Validation:** Validate context matches template before showing → If mismatch → Use generic rationale: "This product matches your selected intent"
- **Error Handling:** Try-catch around rationale generation → Fallback: "This product matches your criteria" → Log errors for debugging

**Rationale template variables (clinical logic):**
- **Allowed placeholders:** `{n}` = number of products viewed in session; `{intent}` = intent label; `{product_title}`, `{product_id}` = current product; `{page_title}` = current page title; `{url}` = current page URL. Optional: `{dwell_sec}`, `{cta_hover_count}`. Backend fills from context; if a variable is missing or invalid, substitute with a safe default or omit that part; if template cannot be filled, use generic rationale.

---

### 7.6 Intent → Block Mapping

| Intent | Default Blocks | Business Logic |
|--------|----------------|----------------|
| **Help me choose** | Shortlist, Recommendation, Trade-off, Action | User needs guidance → show options + recommendation + trade-offs |
| **Compare options** | Comparison, Costs, Benefits, Limitations | User comparing → show side-by-side comparison + key factors |
| **Check eligibility** | Eligibility, Use-Case Fit, Action | User checking fit → show eligibility criteria + use-case match |
| **Understand differences** | Comparison, Trade-off, Examples | User wants clarity → show differences + trade-offs + examples |
| **Just exploring** | Shortlist, Benefits, Custom Query | User browsing → show options + benefits + exploration tools |

**Business Logic:**
- Intent selected → System maps to default blocks
- Blocks auto-assembled in grid
- User can add/remove blocks (v1: fixed mapping, v2: customizable)
- **Block Interactions:** Blocks support drag-and-drop reordering, expand/collapse, removal (see FR-036 to FR-043)

#### 7.6.1 Assembly Logic by Intent (Logical UX Rules)

To keep the experience **efficient, logical, and helpful** on any product site (banking, e-commerce, healthcare, etc.), the **product set** returned by assembly MUST depend on intent. This avoids the logical problem where "Compare options" would show products the user did not interact with.

| Intent | Product set rule | Rationale |
|--------|------------------|------------|
| **Compare options** | **Only** products whose `product_id` is in `context.product_ids` (the set the user viewed/hovered/clicked). No semantic search to add other products. | User expects to compare *exactly* the items they looked at (e.g. X, Y, Z). Showing a different set breaks trust. |
| **Understand differences** | **Only** products in `context.product_ids`. Same as Compare. | Same mental model: clarify differences between *these* products. |
| **Help me choose** | Semantic search (intent + context) → top N products. May use `product_ids` to bias or scope, but can return other relevant products. | User wants a recommendation from the catalog, not restricted to what they viewed. |
| **Just exploring** | Semantic search → top N. Optional category filter from context. | User is browsing; system suggests relevant options. |
| **Check eligibility** | If `context.product_ids` is non-empty: use **only** those products. If empty: semantic search for eligibility-focused content. | When user has been viewing specific products, show eligibility for those; otherwise suggest by relevance. |

**Incomplete "Compare" set (critical for UX):**

- When intent is Compare or Understand differences and one or more `context.product_ids` are **not found** in the index (e.g. page not crawled yet):
  - Return **only the subset found** (e.g. 2 of 3).
  - Show a clear message: e.g. "One product isn't available for comparison (it may not be indexed yet)."
  - Do **not** substitute "popular" or other products as if they were the user's comparison set.
- When **none** of the user's products are found: show "We couldn't load these products for comparison. Try again or choose a different intent." Do not show "popular" under the Compare intent.

**Strip copy (neutral, not assuming intent):**

- When a trigger fires, strip copy MUST describe **behavior only** and invite help, e.g. "You've viewed 2 products — want help?" or "Spent 45 seconds here — want help?"
- Do **not** assume intent in the strip (e.g. avoid "Looks like you're comparing options") so the user chooses intent in the picker without feeling mislabeled.

#### 7.6.2 End-to-End User Flow Diagram (Any Product Site)

The following diagram shows how the main flows work **across any product site** (banking, e-commerce, healthcare, etc.). DAP is product-agnostic; only config (product page rules, categories) and content differ per site.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│              ANY PRODUCT SITE (Banking / E‑commerce / Healthcare / etc.)                 │
│              Customer page + <script> + DecisionPlatform.init({ siteId })                │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│  PAGE LOAD    │               │ USER BROWSES  │               │ TRIGGER FIRES │
│  ───────────  │               │  ───────────  │               │  ───────────  │
│ GET /config   │               │ Events:       │               │ Strip shows   │
│ → Strip +     │               │ • product    │               │ "Want help?   │
│   event       │               │   views      │               │  Click here"   │
│   listeners   │               │ • dwell time │               │       │       │
│               │               │ • CTA hovers │               │       │       │
│ If reload     │               │ • revisits   │               │       ▼       │
│ <5 min:       │               │ Commentary   │               │ User clicks   │
│ "Continue     │               │ strip updates│               │ strip         │
│  where you    │               │ (throttled)  │               │       │       │
│  left off?"   │               │              │               │       ▼       │
└───────┬───────┘               └───────┬─────┘               │ Intent Picker │
        │                               │                       │ (5 options)   │
        │                               └───────────────────────┤       │       │
        │                                                       │       ▼       │
        │                                               User selects intent     │
        │                                                       │       │       │
        │                                                       └───────┼───────┘
        │                                                               │
        │                         POST /assemble { site_id, intent, context }   │
        │                         context = { url, page_title, product_ids[] }  │
        │                                                               │
        ▼                                                               ▼
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                    BACKEND: Assembly logic by intent                                    │
│  ───────────────────────────────────────────────────────────────────────────────────── │
│  Compare options / Understand differences  →  Filter by product_ids ONLY             │
│  (Grid = only products user interacted with: X, Y, Z)                                  │
│                                                                                        │
│  Help me choose / Just exploring            →  Vector (semantic) search, top N        │
│  Check eligibility                           →  product_ids if any; else vector      │
└───────────────────────────────────────────────────────────────────────────────────────┘
        │                                                               │
        │                                                               ▼
        │                       ┌───────────────────────────────────────────────┐
        │                       │ GRID: Blocks + product cards + "Why this?"    │
        │                       │ Block types from intent (e.g. Compare →       │
        │                       │ Comparison, Costs, Benefits, Limitations)    │
        │                       └───────────────────┬───────────────────────────┘
        │                                           │
        │         ┌─────────────────────────────────┼─────────────────────────────────┐
        │         │                                 │                                 │
        │         ▼                                 ▼                                 ▼
        │  Block reorder /                 Empty block:                      Custom query
        │  expand / remove                "Show pricing" etc.               block: search
        │  (sessionStorage)               → pull content                    by feature
        │                                 │                                 │
        └────────────────────────────────┴─────────────────────────────────┘
```

**Flow summary (same on every site):**

1. **Load** → Config fetched → Strip and events start; optional "Continue?" if reload within 5 min.
2. **Browse** → Events and commentary update; no intent assumed.
3. **Trigger** → Strip invites click → Intent picker → User selects one intent.
4. **Assemble** → Backend applies intent-specific rule (user-set only for Compare/Understand; semantic for Help/Explore).
5. **Grid** → Blocks and cards rendered; rationale from templates; block UX and empty/custom-query blocks as configured.

---

### 7.7 Admin Portal

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-026** | **Website Onboarding** | Admin provides website URL | System crawls, extracts, indexes content | Must |
| **FR-027** | **Content Crawling** | Automatic website crawling | Crawl4AI or similar, extract structured/unstructured content | Must |
| **FR-028** | **Vector DB Indexing** | Store content in vector database | Segment by page/product/category, index for RAG | Must |
| **FR-029** | **Content Management** | View/exclude/re-sync content | Admin UI for managing indexed content | Must |
| **FR-030** | **Trigger Configuration** | Configure trigger rules/thresholds | Admin UI for setting trigger parameters | Must |
| **FR-030A** | **Trigger Validation** | Validate trigger configurations | Check thresholds are reasonable, warn if too sensitive | Should |
| **FR-031** | **White-Labeling** | Brand customization | Colors, fonts, logo, copy tone | Should |
| **FR-032** | **Product Page Configuration** | Configure which pages are products | URL patterns, DOM selectors, manual tagging | Must |
| **FR-033** | **Content Freshness Management** | Monitor and refresh stale content | Auto-refresh frequency, stale content alerts, last updated timestamps | Should |

#### 7.7.1 Content & Vector Structure (Multi-Site, Multi-Domain)

DAP serves **different sites and different products in different domains**. RAG must return only that site’s content and build correct product cards. The following structure is required so RAG works properly.

**Isolation per site**

- Each **site** (tenant) has its own content in the vector store. No cross-site results.
- Every search and every indexed chunk is **scoped by site_id**. Different domains (e.g. Site A = banking, Site B = insurance) never mix.

**Structure within a site**

- Content is **segmented by type**: **product** (offerings the user can choose) vs **page** (informational).
- Optionally **category/domain** within site (e.g. "credit-cards", "loans") so RAG can narrow by product line when useful.
- Each stored **chunk** has a **consistent payload schema** (see TAD §11.4) so the assemble pipeline can build product cards (title, features, price, eligibility, etc.) from search results.

**Chunking for retrieval**

- **Products:** Stored so that one product = one or more chunks linked by a stable **product_id**. Text embedded for products includes title, description, and key attributes so semantic search matches user intent and context.
- **Pages:** Informational content chunked (e.g. by section or fixed size with overlap) so RAG can retrieve relevant passages.
- Chunk identity is **deterministic** (e.g. site_id + url + chunk_index) for re-crawl and updates.

**How this makes RAG work properly**

- **Assemble** always filters by **site_id**; optionally by **type** (e.g. product-only) or **category** when context implies it.
- Search returns **points with payload**; backend maps payload fields to **blocks and product cards** (name, features, price, eligibility, URL).
- Different sites and domains stay separate; different product types within a site are distinguishable so the right content is shown for the selected intent.

| Requirement | Purpose |
|--------------|---------|
| **Site-scoped storage** | RAG never returns another site’s products or content. |
| **Type (product vs page)** | Assemble can prefer products for “Help me choose” / “Compare options” and mix in pages when relevant. |
| **Stable product_id** | Deduplicate chunks belonging to the same product; one card per product. |
| **Consistent payload schema** | Same fields across sites/domains so one assemble pipeline can build cards for any site. |
| **Optional category** | Per-site product lines (e.g. cards vs loans) can be filtered when context indicates it. |

**Crawl & index (clinical logic):**
- **Setting product_id and category at crawl time:** For each extracted product/page, crawler sets **product_id** from: URL path slug (e.g. last segment), or Schema.org product ID, or admin-configured selector (e.g. `[data-product-id]`). **Category** from: breadcrumb, Schema.org category, or admin-configured mapping (URL pattern → category). Same rules applied consistently so RAG and assemble can filter and dedupe.
- **Re-crawl strategy (stale point removal):** On re-crawl, upsert points by deterministic chunk_id. After upserting new/changed chunks, **remove points** whose chunk_id no longer exists in the current crawl result (e.g. deleted page or product). This keeps the index in sync with the live site.
- **Excluded URLs:** Admin can set **excluded_url_patterns** (or an explicit list) in site config. Crawler MUST skip URLs matching these patterns; excluded URLs are not fetched and not indexed. Stored in site_config and applied on every crawl.

**Admin defaults & white-label (clinical logic):**
- **Default config for new sites:** When a site is created, backend MUST create a site_config row with default trigger_thresholds, commentary_templates, block_mapping, empty product_page_rules and white_label. Defaults are documented (e.g. multi_product_min=2, dwell_sec=45) so new sites work without admin editing.
- **SDK applying white-label:** SDK MUST apply white_label from config (primary_color, font_family, logo_url, brand_name, copy_tone) to the strip, intent modal, and grid. If a value is missing, use a safe fallback (e.g. neutral gray) so the guide always renders consistently.

---

### 7.8 Website Integration

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-032** | **JavaScript SDK** | Two-line integration | `<script>` tag + `DecisionPlatform.init()` | Must |
| **FR-033** | **Auto-Load** | Guide strip appears automatically | SDK loads on page load, renders strip | Must |
| **FR-034** | **Event Tracking** | Start observing behavior | Event listeners attach on init | Must |
| **FR-035** | **Disable Option** | Remove script to disable | Removing script fully disables platform | Must |

**CORS strategy (clinical logic):**
- Backend MUST allow SDK requests (GET /sdk/config, POST /assemble, GET /sdk/*.js) from **arbitrary customer origins**, because each customer site has a different origin. Options: (a) **allow list per site:** store `allowed_origins` in site_config (e.g. derived from base_url and/or admin-added domains); respond with `Access-Control-Allow-Origin: <origin>` when request Origin matches; (b) **dev:** allow `*` for SDK endpoints. Production: use allow list; do not use `*` with credentials. Document as NFR so multi-tenant embedding is safe.

---

### 7.9 Decision Canvas Block Interactions

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-036** | **Block Drag & Drop** | Users can drag blocks to reorder | Drag handles on each block, visual feedback during drag | Should |
| **FR-037** | **Block Reordering** | Blocks maintain new order | Order persisted in sessionStorage, restored on reload | Should |
| **FR-038** | **Block Expand/Collapse** | Blocks can be expanded or collapsed | Toggle button on each block, preserves state | Should |
| **FR-039** | **Block Removal** | Users can remove unwanted blocks | Remove button (X), confirmation dialog, can re-add later | Should |
| **FR-040** | **Block State Persistence** | Block order and state saved | Stored in sessionStorage, restored within session | Should |

**Business Logic:**
- Drag handles visible on hover or always visible (admin configurable)
- Visual feedback: Block highlights during drag, drop zones shown
- Order persistence: Save to sessionStorage on reorder, restore on page reload (if <5 minutes)
- Expand/collapse: Toggle button expands block to show more details, collapses to summary view
- Removal: X button removes block, shows confirmation: "Remove this block?" → Can re-add from block library
- State management: Track block order, expanded state, removed blocks in sessionStorage

---

### 7.10 Empty Blocks (User-Pulled Content)

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-041** | **Empty Block Display** | Some blocks appear empty with prompts | Blocks show structured prompts instead of content | Must |
| **FR-042** | **Structured Prompts** | Clear prompts guide user action | Template-based prompts: "Want to see [X]? Click here" | Must |
| **FR-043** | **Quick-Select Chips** | Pre-defined options for quick selection | Chips like "Show pricing", "Show benefits", "Show eligibility" | Must |
| **FR-044** | **User-Pulled Content Loading** | Content loads when user clicks prompt | On click → Query Vector DB → Load content into block | Must |
| **FR-045** | **Empty Block Examples** | Examples of empty blocks | Custom Query Block (empty by default), optional blocks | Must |

**Business Logic:**
- Empty blocks appear with structured prompts (no free-form chat required)
- Prompt format: "Want to see [benefits/pricing/eligibility]? Click here" or "Show me [X]"
- Quick-select chips: Pre-defined options user can click (e.g., "Show pricing", "Show benefits", "Compare features")
- Content loading: User clicks prompt/chip → System queries Vector DB for relevant content → Loads into block → Block becomes "filled"
- Purpose: Allow users to pull only what they need, avoid information overload, maintain user control
- Examples: Custom Query Block (always empty), optional blocks in "Just exploring" intent

---

### 7.11 Custom Query Block

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-046** | **Custom Query Block Display** | Empty block with query interface | Shows structured query options, not free-form text | Must |
| **FR-047** | **Structured Query Options** | Pre-defined query categories | Categories: "Find products by...", "Show me...", "Compare..." | Must |
| **FR-048** | **Query Execution** | Execute query and show results | Query Vector DB using structured input, display results in block | Must |
| **FR-049** | **Query Results Display** | Show query results in block | Results displayed as product cards or information blocks | Must |

**Business Logic:**
- Custom Query Block appears empty by default (no content pre-loaded)
- Structured interface: Pre-defined query categories and options (not free-form chat)
- Query categories: "Find products by feature", "Show me products under $X", "Compare products by Y"
- Query execution: User selects query type + parameters → System queries Vector DB → Returns relevant products/content
- Results display: Results shown as product cards or information blocks within the Custom Query Block
- Integration: Uses same RAG system as main grid assembly
- Purpose: Allow users to explore beyond default blocks, pull specific information on demand

---

### 7.12 Session Management

| ID | Feature | Description | Business Logic | Priority |
|----|---------|-------------|----------------|----------|
| **FR-050** | **Session Definition** | Define session boundaries | Session = Browser tab, resets after 30 min idle or page reload | Must |
| **FR-051** | **Session Storage** | Persist state across page reloads | Store intent, grid state, block order in sessionStorage | Should |
| **FR-052** | **Session Timeout** | Reset session after inactivity | 30-minute idle timeout, admin configurable | Must |
| **FR-053** | **SPA Route Handling** | Handle single-page app navigation | Track route changes, reset on major route change | Should |
| **FR-054** | **State Restoration** | Restore state on page reload | If reload <5 minutes → Restore intent and grid state | Should |

**Business Logic:**
- Session = Browser tab (not window), isolated per tab
- Reset conditions: 30 minutes idle, page reload (traditional sites), major route change (SPAs)
- Storage: sessionStorage for intent, selected blocks, block order, grid state
- Restoration: If page reloads within 5 minutes → Restore state → Show "Continue where you left off?" prompt
- SPA handling: Track route changes (hash/pathname), reset session on major route change (e.g., /products → /about)
- Admin configurable: Session timeout (default 30 min), restoration window (default 5 min)

---

## 8. Non-Functional Requirements

### 8.1 Performance

| Requirement | Target | Rationale |
|-------------|--------|-----------|
| **Experience Assembly** | <100ms | Fast grid assembly for seamless UX |
| **Commentary Updates** | <5ms | Real-time commentary without lag |
| **Trigger Detection** | <50ms | Instant trigger response |
| **Vector DB Query** | <80ms | Fast RAG queries for relevance |
| **Lazy Loading** | Progressive | Load blocks as needed, not all at once |

### 8.2 Security & Compliance

| Requirement | Implementation |
|-------------|----------------|
| **Website-Only Content** | Only crawl/admin-approved content |
| **No PII Required** | No personal data collection |
| **GDPR-Friendly** | No identity tracking, session-only data |
| **Enterprise-Safe RAG** | Isolated vector DB namespaces per customer |

### 8.3 Scalability

| Requirement | Implementation |
|-------------|----------------|
| **Multi-Tenant** | Per-site isolation, separate configs |
| **Vector DB Namespace** | One namespace per customer |
| **Horizontal Scaling** | Stateless architecture, load balancing |

### 8.4 Reliability

| Requirement | Target |
|-------------|--------|
| **Uptime** | 99.9% |
| **Error Handling** | Graceful degradation, fallback to basic strip, try-catch around all critical paths | 
| **Data Consistency** | Transactional operations for content sync |
| **Content Freshness** | Auto-refresh frequency configurable, alert if stale >7 days, show last updated timestamp |
| **Configuration Validation** | Validate trigger thresholds (min/max ranges), warn admin if too sensitive, preview trigger frequency |

---

## 9. User Flows

### 9.1 Flow 1: Multiple Product Comparison

**Scenario:** User views 3 credit cards within 5 minutes

**Steps:**
1. User browses website, views "Premium Card A"
   - **Strip shows:** "Viewing Premium Card A..."
2. User navigates to "Premium Card B" (within 2 minutes)
   - **Strip shows:** "You've viewed 2 cards — comparing options?"
3. User views "Premium Card C" (within 5 minutes total)
   - **Trigger fires:** Multiple product views detected
   - **Strip shows:** "Want help comparing? Click here"
4. User clicks strip
   - **Intent menu appears:** 5 intent options
5. User selects "Compare options"
   - **System queries Vector DB:** Finds 4 relevant cards
   - **Grid assembles:** 4 product cards in 2x2 grid
   - **Strip shows:** "Found 4 cards matching your comparison — here's why each fits"
6. User clicks "Why this?" on Card A
   - **Rationale panel shows:** "You viewed 3 premium cards → this offers best rewards for your spending pattern"
7. User reviews grid, makes decision
   - **User clicks CTA** on selected card

**Outcome:** User makes confident decision with clear rationale

---

### 9.2 Flow 2: Hesitation Detection

**Scenario:** User spends 60 seconds on pricing page without clicking CTA

**Steps:**
1. User lands on "Loan Pricing" page
   - **Strip shows:** "Viewing loan pricing..."
2. User scrolls through page, reads content (45 seconds)
   - **Strip shows:** "Spent 45 seconds on pricing — need more info?"
3. User hovers over "Apply Now" button but doesn't click (2 times)
   - **Trigger fires:** CTA hover pattern detected
   - **Strip shows:** "Hovered over Apply Now — want help choosing?"
4. User clicks strip
   - **Intent menu appears**
5. User selects "Check eligibility"
   - **Grid assembles:** Eligibility block + Use-Case Fit + Action blocks
   - **Shows:** Eligibility criteria, matching loans, next steps
6. User reviews eligibility, clicks "Apply"

**Outcome:** User gets clarity on eligibility, proceeds confidently

---

### 9.3 Flow 3: Explicit Help Request

**Scenario:** User clicks "Help me choose" button directly

**Steps:**
1. User browsing products, clicks "Help me choose" button
   - **Trigger fires:** Explicit user trigger (immediate)
2. Intent menu appears immediately
3. User selects "Help me choose"
   - **Grid assembles:** Shortlist + Recommendation + Trade-off + Action blocks
   - **Shows:** Top 3 products, recommendation with rationale, trade-offs, next action
4. User clicks "Why this?" on recommended product
   - **Rationale shows:** "Based on your browsing pattern → this matches your needs best"
5. User reviews, selects product

**Outcome:** Fast path to decision with clear recommendation

---

### 9.4 Flow 4: Edge Case - Multiple Triggers

**Scenario:** Multiple triggers fire simultaneously

**Steps:**
1. User views 2 products (Trigger: Multiple Product Views)
2. User hovers over CTA 2 times (Trigger: CTA Hover Pattern)
3. User spends 45s on page (Trigger: Hesitation Detection)
4. **All triggers fire at same time**
   - **System applies priority:** Explicit > Multiple Products > CTA Hover > Hesitation > Loops
   - **Highest priority trigger wins:** Multiple Product Views (priority 2)
   - **Single intent menu shown:** Based on Multiple Product Views trigger
   - **Other triggers logged:** For analytics but not shown to user
5. User selects intent, grid assembles normally

**Outcome:** Single, clear trigger response without confusion

---

### 9.5 Flow 5: Edge Case - Empty Results

**Scenario:** Vector DB returns 0 products

**Steps:**
1. User selects "Compare options"
2. System queries Vector DB
3. **Query returns 0 products**
   - **Empty state shown:** "No products found matching your criteria"
   - **Options offered:** "Try different intent?" or "Browse all products"
   - **Fallback triggered:** System shows top 3 products by popularity
   - **Message displayed:** "Showing popular options instead"
4. User can try different intent or browse fallback products

**Outcome:** User not stuck, clear path forward

---

### 9.6 Flow 6: Edge Case - Intent Change Mid-Grid

**Scenario:** User changes intent while grid is displayed

**Steps:**
1. User selects "Compare options" → Grid shows comparison blocks
2. User clicks intent selector, changes to "Help me choose"
   - **Grid closes:** Fade out animation
   - **Loading state:** Shows skeleton screens
   - **Grid rebuilds:** With new intent blocks (Shortlist, Recommendation, Trade-off, Action)
   - **Fade in animation:** Smooth transition
3. User sees new grid with different blocks

**Outcome:** Smooth transition, no confusion

---

### 9.7 Flow 7: Edge Case - Page Reload with State

**Scenario:** User reloads page after selecting intent

**Steps:**
1. User selects "Compare options", views grid
2. User accidentally reloads page (within 5 minutes)
   - **System checks sessionStorage:** Finds saved intent and state
   - **Prompt shown:** "Continue where you left off?"
   - **User clicks "Yes":** Grid restores with same intent and products
   - **User clicks "No":** Fresh session starts
3. User continues seamlessly or starts fresh

**Outcome:** No lost progress, user choice

---

## 10. UX Design Details

### 10.1 Commentary Strip Design

**Visual Specifications:**
- **Position:** Fixed bottom, full width
- **Height:** 40-50px
- **Background:** Semi-transparent (90% opacity), brand colors
- **Text:** 14px, readable font, left-aligned
- **Animation:** Smooth fade-in/out on updates
- **Z-index:** High (above page content, below modals)

**Content Format:**
- **Pattern:** "[Action] → [Observation] → [Question]?"
- **Examples:**
  - "You've viewed 3 credit cards in 2 minutes — comparing options?"
  - "Spent 45 seconds on pricing — need more info?"
  - "Hovered over Apply Now — want help choosing?"

**Interaction:**
- **Clickable:** Entire strip is clickable
- **Hover:** Slight background color change
- **Auto-update:** Updates every 2-3 seconds based on behavior

---

### 10.2 Intent Selection UI

**Visual Specifications:**
- **Type:** Modal overlay (centered, 60% width)
- **Background:** Semi-transparent backdrop (80% opacity)
- **Intent Cards:** 5 cards in grid (2x3 or 1x5 on mobile)
- **Card Design:** Rounded corners, hover effects, icons
- **Selection:** Click to select, visual feedback (border/background change)

**Intent Card Layout:**
```
┌─────────────────────┐
│ [Icon]              │
│ Help me choose      │
│ [Description]       │
└─────────────────────┘
```

**Animation:**
- **Appear:** Slide up from bottom
- **Dismiss:** Click outside or X button
- **Selection:** Card expands slightly, checkmark appears

---

### 10.3 Grid Assembly UI

**Visual Specifications:**
- **Layout:** Responsive grid (3 columns desktop, 2 tablet, 1 mobile)
- **Card Size:** Consistent height, variable width
- **Spacing:** 16px gap between cards
- **Animation:** Cards fade in sequentially (staggered)

**Product Card Layout:**
```
┌─────────────────────────────┐
│ [Product Image/Icon]        │
│ Product Name                │
│ ─────────────────────────── │
│ Key Feature 1               │
│ Key Feature 2               │
│ Key Feature 3               │
│ ─────────────────────────── │
│ Price: $XXX                 │
│ Eligibility: ✓ Qualified    │
│ ─────────────────────────── │
│ [Why this?] [CTA Button]    │
└─────────────────────────────┘
```

**Grid Behavior:**
- **Loading:** Skeleton screens while querying
- **Empty State:** "No products found" message
- **Scroll:** Infinite scroll if >5 products (v2)

---

### 10.4 Rationale Panel UI

**Visual Specifications:**
- **Type:** Side panel (slides from right) or inline expansion
- **Width:** 400px (desktop), full width (mobile)
- **Background:** Light background, readable text
- **Close:** X button or click outside

**Rationale Content Layout:**
```
┌─────────────────────────────┐
│ Why this product?        [X] │
│ ─────────────────────────── │
│ [Icon] You viewed 2 similar │
│ products → this matches     │
│ your comparison pattern     │
│ ─────────────────────────── │
│ [Icon] You spent time on    │
│ pricing → this offers best  │
│ value                       │
│ ─────────────────────────── │
│ [Icon] Based on your        │
│ browsing → this fits your   │
│ use case                    │
└─────────────────────────────┘
```

**Visual Elements:**
- **Icons:** Checkmarks, arrows, info icons
- **Formatting:** Bullet points, clear hierarchy
- **Tone:** Friendly, helpful, transparent

---

### 10.5 Responsive Design

| Screen Size | Strip | Intent Menu | Grid | Rationale Panel |
|-------------|-------|-------------|------|-----------------|
| **Desktop (>1024px)** | Full width, 50px height | Modal, 60% width | 3 columns | Side panel, 400px |
| **Tablet (768-1024px)** | Full width, 45px height | Modal, 80% width | 2 columns | Side panel, 350px |
| **Mobile (<768px)** | Full width, 40px height | Full screen modal | 1 column | Bottom sheet |

---

### 10.6 Decision Canvas Block Interactions UX

**Visual Specifications:**
- **Drag Handles:** Visible on hover (or always visible, admin configurable), icon indicator
- **Drop Zones:** Visual indicators show where block can be dropped
- **Expand/Collapse:** Toggle button (chevron icon), smooth animation
- **Remove Button:** X button in top-right corner, confirmation dialog on click
- **State Persistence:** Visual indicator shows saved state (checkmark icon)

**Interaction Patterns:**
- **Drag:** Click and hold drag handle → Drag block → Drop in new position → Visual feedback (highlight, animation)
- **Reorder:** Blocks reorder smoothly, order saved automatically
- **Expand:** Click expand button → Block expands to show full content → Collapse button appears
- **Remove:** Click X → Confirmation dialog → Confirm → Block removed → Can re-add from block library

---

### 10.7 Empty Blocks UX

**Visual Specifications:**
- **Empty State:** Light background, centered content, clear call-to-action
- **Prompt Text:** Large, readable, action-oriented (e.g., "Want to see pricing?")
- **Quick-Select Chips:** Rounded chips, hover effects, clickable
- **Loading State:** Skeleton screen while content loads

**Layout Example:**
```
┌─────────────────────────────┐
│                             │
│   Want to see pricing?      │
│                             │
│  [Show Pricing] [Benefits]  │
│  [Eligibility] [Compare]    │
│                             │
└─────────────────────────────┘
```

**Interaction:**
- User clicks chip → Block shows loading state → Content loads → Block becomes "filled"
- User can click multiple chips to load multiple content types

---

### 10.8 Custom Query Block UX

**Visual Specifications:**
- **Query Interface:** Dropdown/select for query category, input fields for parameters
- **Query Categories:** "Find products by feature", "Show products under $X", "Compare by Y"
- **Results Display:** Product cards or information blocks within the Custom Query Block
- **Loading State:** Skeleton screens while query executes

**Layout Example:**
```
┌─────────────────────────────┐
│ Custom Query                │
│ ─────────────────────────── │
│ Find products by: [Feature ▼]│
│ Feature: [Search...]        │
│ [Search]                    │
│ ─────────────────────────── │
│ [Results appear here]       │
└─────────────────────────────┘
```

**Interaction:**
- User selects query category → Enters parameters → Clicks "Search" → Results load in block
- Results displayed as product cards or information blocks

---

## 11. Conclusion

### 11.1 Success Criteria

The Decision Assembly Platform will be considered successful if:

1. **Decision Time Reduction:** Users make decisions 40% faster
2. **Conversion Uplift:** CTA conversion increases by 25%
3. **Bounce Rate Reduction:** Product page bounce rate decreases by 30%
4. **User Engagement:** 60%+ users interact with grid/rationale
5. **Trust Building:** Users understand why products are shown

### 11.2 Key Differentiators

- **Experience IS the product** — Not a tool, but an experience layer
- **No conversation needed** — Structured blocks, not chat
- **Transparent rationale** — Every recommendation explained
- **Zero-code integration** — Two lines of JavaScript
- **Deterministic triggers** — Rule-based, not ML prediction (v1)

---

**Document End**

---

*Generated using Bmad PM Agent: `Rules/.bmad-core/agents/pm.md`*  
*Version 1.1 - Edge Cases & Missing Features Fixed*
