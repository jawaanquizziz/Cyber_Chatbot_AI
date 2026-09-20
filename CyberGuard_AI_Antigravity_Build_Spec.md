# CyberGuard AI --- Antigravity Build Specification

## Developer Brief

Build **CyberGuard AI**, a professional web application for
cybersecurity awareness and suspicious-message analysis.

This is an **academic prototype with a real purpose**: help a user
understand potentially suspicious messages such as phishing attempts,
fake job offers, delivery scams, impersonation messages, and credential
requests.

The application must demonstrate the NLP concepts from the supplied
academic paper:

-   Natural Language Understanding
-   Intent Detection
-   Entity Extraction
-   Contextual Conversation
-   Information Retrieval
-   AI-generated Response
-   Task-oriented Dialogue

The result must look like a **real product built by a developer for a
defined cybersecurity use case**.

------------------------------------------------------------------------

# 1. VERY IMPORTANT DESIGN DIRECTION

## Do NOT make this look AI-generated.

Avoid the typical "AI project" visual style:

-   No excessive glowing gradients
-   No giant futuristic robot graphics
-   No floating AI brain illustrations
-   No unnecessary neon effects
-   No excessive glassmorphism
-   No random animated particles
-   No oversized "AI POWERED" labels
-   No generic ChatGPT clone interface
-   No excessive rounded cards everywhere
-   No fake statistics
-   No meaningless dashboard charts
-   No decorative elements that do not serve the product

The interface should feel like it was designed by an experienced product
engineer and UI/UX designer for an actual cybersecurity product.

Think:

-   Security software
-   Developer tooling
-   Professional SaaS
-   Security operations interface
-   Enterprise internal security utility

The visual language should be **quiet, precise, functional and
trustworthy**.

Prioritize:

-   Information hierarchy
-   Typography
-   Spacing
-   Clear states
-   Strong interaction design
-   Consistent components
-   Accessibility
-   Responsive behavior
-   Useful micro-interactions
-   Clear error handling

The application should look like a product that could genuinely be used
by a college IT department, small company, or cybersecurity awareness
team.

------------------------------------------------------------------------

# 2. PRODUCT NAME

**CyberGuard**

Subtitle:

**Message Security Analysis**

Do not repeatedly use "AI" in the interface.

The product can be described as:

> Analyze suspicious messages and understand the signals behind them.

Use "AI-assisted analysis" only where technically relevant.

------------------------------------------------------------------------

# 3. PRODUCT PURPOSE

The user pastes a suspicious message.

CyberGuard analyzes it and presents:

1.  Risk assessment
2.  Detected intent
3.  Extracted entities
4.  Suspicious indicators
5.  Explanation
6.  Recommended actions

The user can then ask follow-up questions about the analysis.

Example:

User:

> URGENT: Your account will be blocked today. Verify your account
> immediately by clicking this link and entering your OTP.

CyberGuard should identify signals such as:

-   Urgency
-   Account suspension pressure
-   External link
-   OTP request
-   Credential-related action

The system must use careful wording:

-   "Potential phishing indicators detected"
-   "This message appears suspicious"
-   "Risk assessment: High"

Never claim that the system has definitively proven a message is
malicious.

------------------------------------------------------------------------

# 4. CORE USER EXPERIENCE

The primary workflow should be extremely clear:

``` text
Paste message
      ↓
Analyze
      ↓
Review assessment
      ↓
Understand why
      ↓
Take safe action
      ↓
Ask follow-up questions
```

Do not make users navigate through unnecessary pages before performing
the main task.

The message analyzer should be the primary screen.

------------------------------------------------------------------------

# 5. APPLICATION STRUCTURE

Create:

### Main navigation

-   Analyze
-   History
-   Security Guide
-   About

Keep navigation minimal.

Do not create pages just to make the application appear larger.

------------------------------------------------------------------------

# 6. MAIN ANALYZE PAGE

Create a professional application shell.

### Header

Left:

**CyberGuard**

Small text:

`Message Security Analysis`

Right:

-   System status indicator
-   Theme control only if it genuinely improves usability
-   Minimal navigation

Avoid unnecessary profile/avatar UI.

------------------------------------------------------------------------

# 7. ANALYZER LAYOUT

Desktop layout:

``` text
-----------------------------------------------------
| CyberGuard                           System: Ready |
-----------------------------------------------------
|                                                   |
| Analyze a message                                |
| Understand suspicious signals before taking      |
| action.                                          |
|                                                   |
| -----------------------   ---------------------- |
| | Paste message here  |   | Assessment          | |
| |                     |   |                     | |
| |                     |   | Waiting for input  | |
| |                     |   |                     | |
| -----------------------   ---------------------- |
|                                                   |
-----------------------------------------------------
```

Use a balanced two-column layout on desktop.

On mobile, stack the sections vertically.

------------------------------------------------------------------------

# 8. INPUT COMPONENT

Large but not oversized textarea.

Placeholder:

> Paste the message you want to analyze...

Below it:

Character count.

Buttons:

**Analyze message**

**Load example**

**Clear**

Do not use excessive button variations.

Primary action should be visually obvious.

------------------------------------------------------------------------

# 9. EXAMPLE MESSAGES

Provide a small "Try an example" control.

Examples:

### Banking

> URGENT: Your bank account will be suspended today. Verify your account
> immediately using the link below and enter your OTP.

### Job offer

> Congratulations! You have been selected for a work-from-home position.
> Pay ₹2,499 as a registration fee to complete your application.

### Delivery

> Your parcel could not be delivered. Pay ₹49 to reschedule your
> delivery using the link below.

### Malware

> Your friend sent you an important document. Download the attached APK
> and install it to view the file.

### Benign

> Hi, the college assignment submission deadline is tomorrow at 5 PM.

Include at least two benign examples.

The system must not classify every message as suspicious.

------------------------------------------------------------------------

# 10. ANALYSIS RESULT

After analysis, replace the empty state with a structured assessment.

Do not make the result look like a chatbot response.

Make it look like a professional security assessment.

Example:

## Assessment

**Potential Phishing**

`HIGH RISK`

Supporting text:

> The message contains several signals commonly associated with phishing
> attempts.

Then show separate sections.

------------------------------------------------------------------------

# 11. RISK SECTION

Use clear semantic status styles:

### Low

Neutral/green treatment.

### Medium

Amber treatment.

### High

Red treatment.

Do not use flashing animations.

Do not make the entire screen red for high risk.

Only the relevant status elements should use warning styling.

------------------------------------------------------------------------

# 12. INTENT DETECTION

Section title:

**Detected intent**

Example:

`Credential / account verification`

Supporting explanation:

> The sender is attempting to persuade the recipient to provide
> account-related information.

This demonstrates NLP intent detection.

------------------------------------------------------------------------

# 13. ENTITY EXTRACTION

Section:

**Detected entities**

Display compact structured rows or tags.

Possible entity types:

-   Organization
-   Person
-   URL
-   Email
-   Phone
-   Money
-   Date
-   Requested information
-   Action

Example:

``` text
Organization       SBI
URL                example.com
Requested data     OTP
Action             Verify account
Urgency             Immediate
```

Do not create fake entities.

Only display entities detected by the implemented analysis.

------------------------------------------------------------------------

# 14. INDICATORS

Section:

**Why this message was flagged**

Each indicator should contain:

### Indicator

Urgency

### Explanation

The message pressures the recipient to act immediately.

Possible indicators:

-   Urgency
-   Threat of account suspension
-   Credential request
-   OTP request
-   Suspicious URL
-   Impersonation
-   Unusual payment request
-   Unexpected attachment
-   Pressure to install software
-   Prize claim
-   Job registration fee

Only show indicators actually detected.

------------------------------------------------------------------------

# 15. RECOMMENDED ACTIONS

Section:

**Recommended next steps**

Use concise, practical actions.

Example:

1.  Do not click the link.
2.  Do not provide an OTP or password.
3.  Verify the request through the organization's official website or
    contact channel.
4.  Report the message if appropriate.

Do not provide dangerous instructions.

------------------------------------------------------------------------

# 16. FOLLOW-UP CHAT

Only show the conversational section after an analysis exists.

Title:

**Ask about this assessment**

Description:

> Ask CyberGuard why something was flagged or what you should do next.

Suggested questions:

-   Why was this flagged?
-   What information is the sender trying to obtain?
-   What should I do next?
-   Which part of the message is suspicious?
-   How can I verify this safely?

The conversation must use the current analysis as context.

This demonstrates contextual conversational AI.

The chat UI should be compact and secondary to the analysis.

Do NOT make the entire product look like a ChatGPT clone.

------------------------------------------------------------------------

# 17. NLP IMPLEMENTATION

Use a hybrid implementation.

## Deterministic NLP preprocessing

Use Python to extract obvious entities and signals:

-   URLs
-   Email addresses
-   Phone numbers
-   Monetary values
-   OTP references
-   Urgency phrases
-   Password requests
-   Account verification requests
-   Payment requests

Use regex and carefully maintained patterns.

## AI analysis

Use Gemini through the backend for:

-   Intent detection
-   Threat category
-   Context understanding
-   Explanation
-   Recommended actions
-   Follow-up conversation

The model must return structured JSON.

------------------------------------------------------------------------

# 18. AI RESPONSE SCHEMA

Use a strict response schema similar to:

``` json
{
  "category": "Potential Phishing",
  "risk_level": "HIGH",
  "intent": "Credential Theft",
  "entities": [
    {
      "type": "ORGANIZATION",
      "value": "SBI"
    },
    {
      "type": "URL",
      "value": "example.com"
    },
    {
      "type": "REQUESTED_INFORMATION",
      "value": "OTP"
    }
  ],
  "indicators": [
    {
      "name": "Urgency",
      "explanation": "The message pressures the recipient to act immediately."
    }
  ],
  "recommended_actions": [
    "Do not click the link.",
    "Do not share OTPs or passwords.",
    "Verify the request through an official channel."
  ],
  "explanation": "The message contains several signals commonly associated with phishing."
}
```

Validate the response before returning it to the frontend.

If the AI returns malformed JSON, handle it gracefully.

------------------------------------------------------------------------

# 19. BACKEND

Use:

-   Python
-   FastAPI
-   Gemini API

Architecture:

``` text
React
  ↓
FastAPI
  ↓
Preprocessing
  ↓
Rule-based entity extraction
  ↓
Gemini analysis
  ↓
Knowledge base lookup
  ↓
Validated JSON
  ↓
React
```

API endpoints:

``` text
GET  /api/health
POST /api/analyze
POST /api/chat
```

------------------------------------------------------------------------

# 20. SECURITY

Never expose the Gemini API key in React.

Use:

``` text
GEMINI_API_KEY=
```

in `.env`.

Create `.env.example`.

Never commit secrets.

Never execute URLs provided by users.

Never download files supplied through analyzed text.

Never visit external links during analysis.

Treat all submitted messages as untrusted text.

------------------------------------------------------------------------

# 21. CYBERSECURITY KNOWLEDGE BASE

Create a small local knowledge base.

Categories:

-   Phishing
-   Smishing
-   Vishing
-   Credential Theft
-   Social Engineering
-   Job Scams
-   Delivery Scams
-   Banking Scams
-   Investment Scams
-   Malware
-   Impersonation

Each entry should contain:

-   Definition
-   Common indicators
-   Safe response
-   Prevention advice

Keep the content concise and practical.

------------------------------------------------------------------------

# 22. HISTORY

Create a simple history page.

Store recent analyses in localStorage.

Each record:

-   Timestamp
-   Message preview
-   Category
-   Risk level

Clicking a record should reopen the analysis.

Provide:

**Clear history**

Do not store unnecessary sensitive information.

------------------------------------------------------------------------

# 23. SECURITY GUIDE

Create a useful reference page.

Topics:

### Phishing

What it is and common warning signs.

### Suspicious links

How to verify links safely.

### OTP and passwords

Why they should never be shared.

### Job scams

Common fee/payment patterns.

### Delivery scams

Fake rescheduling/payment messages.

### Impersonation

How attackers create urgency.

### Attachments

Why unknown files can be dangerous.

The page should feel like product documentation, not an AI-generated
blog.

------------------------------------------------------------------------

# 24. ABOUT PAGE

Keep it short.

Explain:

> CyberGuard is an academic prototype demonstrating how Natural Language
> Processing and conversational AI can support cybersecurity awareness.

Then show:

### NLP techniques demonstrated

-   Intent recognition
-   Entity extraction
-   Context-aware dialogue
-   Natural language understanding
-   AI response generation
-   Knowledge retrieval

Also state:

> CyberGuard provides an AI-assisted assessment and should not be
> treated as definitive proof that a message is malicious or safe.

------------------------------------------------------------------------

# 25. RESPONSIBLE AI

Include a subtle disclaimer near the analyzer:

> AI-assisted assessment. Verify important messages through trusted
> official channels.

Do not make the disclaimer dominate the UI.

Never encourage users to provide:

-   Passwords
-   OTPs
-   Authentication codes
-   Bank credentials
-   API keys
-   Private keys

------------------------------------------------------------------------

# 26. DEMO MODE

The application must work even without a Gemini API key.

Create a **Demo Mode** using predefined analysis results.

This is important for the academic presentation.

Demo flow:

1.  Load suspicious banking message.
2.  Analyze.
3.  Show high-risk assessment.
4.  Show intent.
5.  Show entities.
6.  Show indicators.
7.  Show recommended actions.
8.  Ask "Why was this flagged?"
9.  Show contextual response.
10. Analyze a benign message.
11. Show that the system can return a lower-risk assessment.

Make Demo Mode feel like a legitimate offline/demo capability, not a
fake UI.

------------------------------------------------------------------------

# 27. LOADING STATE

During real analysis:

Show a compact status area:

``` text
Analyzing message

Processing text
Detecting intent
Extracting entities
Assessing indicators
Preparing assessment
```

Use subtle progress indicators.

Do not use exaggerated AI animations.

------------------------------------------------------------------------

# 28. EMPTY STATES

Create thoughtful empty states.

Example:

### No analysis yet

> Paste a message to begin.

Secondary text:

> CyberGuard will identify possible intent, entities and security
> indicators.

Do not use robot illustrations.

------------------------------------------------------------------------

# 29. ERROR STATES

Handle:

-   Empty message
-   Very long message
-   API unavailable
-   Backend unavailable
-   Timeout
-   Invalid AI response
-   Network error

Example:

> Analysis could not be completed.

Then:

**Try again**

and:

**Use demo mode**

Do not display raw stack traces to users.

------------------------------------------------------------------------

# 30. VISUAL SYSTEM

Create a consistent design system.

Use:

-   One primary font family
-   One mono font for technical values if useful
-   Consistent spacing scale
-   Consistent border radius
-   Consistent button styles
-   Consistent status colors

Suggested style:

-   Background: near-black/navy
-   Surface: slightly lighter dark gray
-   Borders: subtle gray
-   Text: off-white
-   Secondary text: muted gray
-   Accent: restrained blue
-   Warning: amber
-   Danger: red
-   Safe: green

Do not hard-code dozens of unrelated colors.

------------------------------------------------------------------------

# 31. COMPONENT QUALITY

Create reusable components:

``` text
AppShell
TopNav
MessageInput
ExampleSelector
AnalysisSummary
RiskBadge
IntentCard
EntityList
IndicatorList
RecommendedActions
FollowUpChat
HistoryList
SecurityTipCard
EmptyState
ErrorState
LoadingState
```

Avoid giant monolithic components.

Keep the code maintainable.

------------------------------------------------------------------------

# 32. RESPONSIVE BEHAVIOR

Desktop:

Two-column analysis workspace.

Tablet:

Reduced spacing and stacked secondary panels where appropriate.

Mobile:

Single-column layout.

Ensure:

-   No horizontal overflow
-   Buttons remain accessible
-   Textareas are usable
-   Cards do not become excessively tall
-   Navigation remains usable
-   Tables become mobile-friendly

------------------------------------------------------------------------

# 33. ACCESSIBILITY

Implement:

-   Semantic HTML
-   Proper labels
-   Keyboard navigation
-   Visible focus states
-   Accessible contrast
-   ARIA labels where appropriate
-   Screen-reader-friendly status messages

------------------------------------------------------------------------

# 34. PERFORMANCE

Avoid unnecessary libraries.

Do not install a library just for a simple UI feature.

Keep:

-   API calls controlled
-   Components lightweight
-   Animations minimal
-   Bundle reasonable

Do not build unnecessary real-time infrastructure.

------------------------------------------------------------------------

# 35. PROJECT STRUCTURE

Use:

``` text
cyberguard/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── data/
│   │   ├── hooks/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── nlp/
│   │   ├── models/
│   │   ├── knowledge/
│   │   └── main.py
│   └── requirements.txt
│
├── .env.example
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

# 36. README

Create a professional README.

Sections:

1.  CyberGuard
2.  Problem
3.  Objective
4.  Features
5.  NLP concepts
6.  Architecture
7.  Tech stack
8.  Setup
9.  Environment variables
10. Running locally
11. API endpoints
12. Demo
13. Limitations
14. Future improvements

Include Mermaid architecture.

Do not claim production-grade detection.

Do not claim unsupported accuracy.

------------------------------------------------------------------------

# 37. ACADEMIC CONNECTION

The implementation must clearly demonstrate the concepts from the
provided NLP paper.

Map them as:

  -----------------------------------------------------------------------
  NLP Concept                         CyberGuard Implementation
  ----------------------------------- -----------------------------------
  Natural Language Understanding      Understands message meaning and
                                      security context

  Intent Detection                    Identifies likely purpose of the
                                      message

  Entity Extraction                   Extracts URLs, organizations,
                                      email, money, requested information
                                      etc.

  Contextual Interaction              Follow-up questions use the current
                                      analysis

  Information Retrieval               Uses cybersecurity knowledge base

  Response Generation                 AI generates explanation and
                                      recommendations

  Task-oriented Dialogue              Guides the user toward safe next
                                      actions
  -----------------------------------------------------------------------

Do not invent results from the paper.

If discussing the paper's reported metrics, clearly label them as
**paper-reported results**, not CyberGuard results.

------------------------------------------------------------------------

# 38. EVALUATION

Create a small evaluation section in the application documentation.

Use manually testable cases:

  Test                     Expected behavior
  ------------------------ -----------------------------------------------
  Banking phishing         Detect phishing-related signals
  Job scam                 Detect payment/job-scam indicators
  Delivery scam            Detect suspicious payment/link behavior
  Malware message          Detect suspicious software/attachment request
  Benign college message   Avoid automatically marking it malicious

Do not fabricate percentages.

Do not create fake benchmark charts.

------------------------------------------------------------------------

# 39. DEVELOPMENT QUALITY

The code must look like it was written by a developer.

That means:

-   Clear naming
-   Small components
-   Meaningful comments only
-   No excessive comments explaining obvious code
-   Proper error handling
-   No duplicate code
-   No placeholder lorem ipsum
-   No fake metrics
-   No unused buttons
-   No dead navigation
-   No console errors
-   No broken links
-   No unfinished sections
-   No "Coming Soon" features unless genuinely necessary

Every visible interaction should either work or not exist.

------------------------------------------------------------------------

# 40. FINAL TESTING

After building:

1.  Install frontend dependencies.
2.  Install backend dependencies.
3.  Start backend.
4.  Start frontend.
5.  Test `/api/health`.
6.  Test a phishing example.
7.  Test a benign example.
8.  Test entity extraction.
9.  Test follow-up conversation.
10. Test history.
11. Test demo mode.
12. Test API failure.
13. Test mobile layout.
14. Check browser console.
15. Fix all runtime errors.

Then provide the exact commands needed to run the application.

------------------------------------------------------------------------

# 41. FINAL PRODUCT STANDARD

The final result should feel like:

> "A focused cybersecurity utility with an NLP engine."

Not:

> "A student made an AI chatbot."

The product should be restrained, intentional, technically credible and
visually polished.

Every design decision should support the actual purpose of helping users
understand suspicious messages.

Build the application completely rather than producing a static mockup.
