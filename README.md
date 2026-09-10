# LabelSetu – Product Label Compliance Verification System

An automated verification system designed for Smart India Hackathon (SIH 2026) to detect, analyze, and validate mandatory compliance details on packaged goods labels under the Legal Metrology (Packaged Commodities) Rules, 2011.

## 1. Project Information

- **Project Title:** LabelSetu – Automated Packaged Goods Label Compliance Verification
- **PS ID:** SIH26034
- **PS Title:** Software System to check compliance of Packaged Commodities under Legal Metrology (Packaged Commodities) Rules, 2011 by scanning products, images and labels.
- **Team Name:** 404pass
- **Category:** Software
- **Theme:** Miscellaneous

## 2. Problem Statement

Mandatory label declarations are required under the Legal Metrology (Packaged Commodities) Rules, 2011. Missing or incomplete declarations are common due to packaging design oversight, shifting regulatory norms, or lack of accessible verification tools. 

Manual checking across thousands of retail items is slow, inconsistent, and rule-dependent. Non-compliance leads to regulatory penalties, product recalls, and costly reprint corrections. Currently, no simple, self-serve pre-print verification tool exists for manufacturers, packers, and sellers.

## 3. Proposed Solution

LabelSetu works on the principle of Automated Label Information Extraction and Rule-Based Compliance Verification:

1. **Label Capture:** A product label is captured or uploaded as an image.
2. **OCR Text Extraction:** Optical Character Recognition (OCR) extracts textual information from the label and identifies important fields such as MRP, net quantity, manufacturer details, dates, and consumer care information.
3. **Category-Based Rule Mapping:** The selected product category determines the set of mandatory declarations required under the Legal Metrology (Packaged Commodities) Rules, 2011.
4. **Missing Declaration Detection:** The system compares extracted fields against mandatory requirements using a rule-based compliance engine, identifying which declarations are present and which are missing.
5. **Report & History:** The result is presented as a clear Pass/Fail status with a Found vs. Missing breakdown and saved in a historical audit log.
6. **Modular Architecture:** The rule engine is decoupled from the OCR technology, allowing text-extraction models to improve independently without altering compliance logic.

## 4. Key Features

- Product label image upload (supports JPEG, PNG, WebP)
- Optical Character Recognition (OCR) text extraction
- Category-based rule mapping (Legal Metrology Packaged Commodities Rules, 2011)
- Mandatory declaration detection with Found vs. Missing breakdown
- Real-time Pass / Fail validation status and structured verification report
- User authentication with secure JWT session management
- Historical audit dashboard with individual scan inspection
- Database-backed dynamic compliance rule management

## 5. Technology Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Node.js, Express.js
- **File Handling:** Multer
- **Database:** MongoDB Atlas (Mongoose ODM)
- **OCR / Computer Vision:** OCR Service Interface / Python CV microservice (OpenCV, Tesseract)
- **Authentication:** JSON Web Tokens (JWT), bcryptjs

## 6. Architecture

See [docs/architecture.md](docs/architecture.md).

```text
User / Inspector
      │
      ▼
Frontend (HTML / CSS / JS)
      │
      ▼
Backend REST API (Node.js & Express)
      ├───► MongoDB Atlas (Users, Compliance Rules, Scan History)
      │
      ▼
OCR & Field Extraction Engine
      │
      ▼
Compliance Engine (Legal Metrology Rules 2011)
      │
      ▼
Audit Report & Verification Dashboard (PASS / FAIL)
```

## 7. Repository Structure

```text
SIH/
├── README.md
├── .gitignore
├── LICENSE
├── Frontend/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── results.html
│   ├── style.css
│   └── app.js
├── Backend/
│   ├── server.js
│   ├── app.js
│   ├── package.json
│   ├── .env.example
│   ├── config/
│   │   ├── db.js
│   │   └── env.js
│   ├── models/
│   │   ├── User.js
│   │   ├── Scan.js
│   │   └── ComplianceRule.js
│   ├── routes/
│   │   ├── auth.routes.js
│   │   ├── verify.routes.js
│   │   └── dashboard.routes.js
│   ├── controllers/
│   │   ├── auth.controller.js
│   │   ├── verify.controller.js
│   │   └── dashboard.controller.js
│   ├── services/
│   │   ├── rules.service.js
│   │   ├── verification.service.js
│   │   ├── auth.service.js
│   │   ├── ocr.service.js
│   │   └── cvClient.js
│   ├── data/
│   │   ├── userStore.js
│   │   └── scanStore.js
│   ├── middleware/
│   │   ├── auth.middleware.js
│   │   ├── error.middleware.js
│   │   └── upload.middleware.js
│   └── scripts/
│       └── seed.js
├── cv_service/
└── legalmetrology_part3/
```

### What goes where?

| Item | Location |
|---|---|
| Frontend client | `Frontend/` |
| Express API & Database models | `Backend/` |
| CV / OCR microservice | `cv_service/` & `legalmetrology_part3/` |
| Compliance rule seed script | `Backend/scripts/seed.js` |
| Project overview | `README.md` |

## 8. Final Presentation

Keep your final SIH presentation in the repository whenever the file size allows it.

- **Presentation Link (Canva):** [View Team 404pass SIH Presentation](https://www.canva.com/design/DAHUmSoMgMo/RKKyxu2Sck6mA3cuA8gCRA/view)
- See [submission/PRESENTATION.md](submission/PRESENTATION.md) for the required format.

If the PPT is too large for GitHub, use Google Drive/OneDrive and put the accessible viewer link in `submission/PRESENTATION.md`.

## 9. Demo Video

YouTube link: [submission/DEMO.md](submission/DEMO.md).
https://www.youtube.com/watch?v=Rpcbo7eagqo

## 10. Screenshots / Prototype Photos

Add important screenshots or hardware/prototype photos to:

`assets/screenshots/`

See [assets/screenshots/README.md](assets/screenshots/README.md) for examples and naming conventions.

## 11. Installation

```bash
# Clone the repository
git clone https://github.com/Daksh1879/SIH.git
cd SIH/Backend

# Install dependencies
npm install

# Configure environment variables
cp .env.example .env
# Edit .env and set MONGO_URI and JWT_SECRET
```

## 12. Run

```bash
# Populate compliance rules in MongoDB Atlas
npm run seed

# Start development server
npm run dev

# Or start production server
npm start
```

Access the frontend by opening `Frontend/index.html` or running a local static server.

## 13. Future Scope

- Multilingual OCR supporting regional Indian languages on packaging labels.
- Barcode and QR code cross-referencing with official national registration databases.
- Automated nutritional information table parsing and allergen declaration checks.
- Mobile application for real-time edge scanning by field inspectors, manufacturers, and consumers.

## Important

Before submission, make sure the repository is accessible to reviewers. Do **not** upload passwords, API keys, access tokens, `.env` files containing secrets, or other confidential credentials.
