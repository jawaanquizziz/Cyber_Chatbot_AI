export const SECURITY_GUIDE = [
  {
    key: 'phishing',
    title: 'Phishing',
    icon: '🎣',
    definition:
      'Phishing is a deceptive attempt to steal sensitive information by impersonating a trusted entity through email, SMS, or messaging platforms.',
    indicators: [
      'Urgent language pressuring immediate action',
      'Requests for OTPs, passwords, or account details',
      'Links to lookalike websites mimicking legitimate organizations',
      'Threats of account suspension or legal action',
      'Unexpected verification requests from unknown senders',
    ],
    safeResponse:
      'Do not click any links. Do not provide personal information. Verify the request by contacting the organization directly through their official website or customer care number.',
    prevention:
      'Enable two-factor authentication. Bookmark official websites. Always verify sender domains. Report suspicious messages to your bank or IT team.',
  },
  {
    key: 'links',
    title: 'Suspicious Links',
    icon: '🔗',
    definition:
      'Attackers use lookalike URLs, shortened links, or slightly misspelled domains to redirect victims to fraudulent websites designed to capture credentials or install malware.',
    indicators: [
      'Domain is slightly different from the official website (e.g., sbi-verify.com vs sbi.co.in)',
      'URL uses HTTP instead of HTTPS',
      'Shortened links that hide the destination (bit.ly, tinyurl)',
      'Unusual subdomains (secure.sbi.verify-now.com)',
      'Unexpected country-code domains (.xyz, .tk, .ru)',
    ],
    safeResponse:
      'Hover over links to preview the destination. Type the organization\'s URL directly into your browser rather than clicking a link in a message.',
    prevention:
      'Use a browser that displays the full URL. Check that the domain exactly matches the official organization. When in doubt, do not click.',
  },
  {
    key: 'otp',
    title: 'OTPs and Passwords',
    icon: '🔐',
    definition:
      'OTPs (One-Time Passwords) and passwords are personal authentication factors. Sharing them with anyone — including people claiming to be bank staff or support agents — grants full access to your account.',
    indicators: [
      'Any request to share an OTP over a call or message',
      'Claim that sharing the OTP is required to "verify" or "unblock" your account',
      'Request arrives immediately after you receive a real OTP',
      'Caller or message creates urgency around entering the OTP',
    ],
    safeResponse:
      'Never share an OTP with anyone. OTPs should only be entered on the official app or website that generated the request.',
    prevention:
      'No legitimate bank, government agency, or service provider will ever ask for your OTP. This is an absolute rule with no exceptions.',
  },
  {
    key: 'jobs',
    title: 'Job Scams',
    icon: '💼',
    definition:
      'Job scams offer fake work-from-home or freelance positions and ask victims to pay registration fees, processing fees, or training costs before any work or payment is received.',
    indicators: [
      'Unsolicited job offer via WhatsApp, SMS, or Telegram',
      'Request to pay a fee before starting work',
      'Unusually high pay for minimal or undefined work',
      'Tasks involve liking videos, completing surveys, or rating products',
      'No verifiable company address or official website',
    ],
    safeResponse:
      'Legitimate employers do not charge applicants. Do not pay any registration or processing fee. Report to cybercrime.gov.in.',
    prevention:
      'Only apply to jobs through verified platforms. Research the company independently. Never pay money to get a job.',
  },
  {
    key: 'delivery',
    title: 'Delivery Scams',
    icon: '📦',
    definition:
      'Delivery scams impersonate courier services and send fake notifications about undelivered parcels, asking recipients to pay small fees to reschedule delivery or update their address.',
    indicators: [
      'Unexpected delivery failure notification with no prior order',
      'Request to pay a small fee (₹20–₹99) to reschedule',
      'Link that does not match the official courier domain',
      'No tracking number or order reference provided',
    ],
    safeResponse:
      'Go directly to the official courier website and track your order using your tracking number. Do not click links in unsolicited SMS messages.',
    prevention:
      'Legitimate couriers do not request redelivery fees through SMS links. Always verify through the official courier app or website.',
  },
  {
    key: 'impersonation',
    title: 'Impersonation',
    icon: '🎭',
    definition:
      'Impersonation attacks involve an attacker pretending to be a bank, employer, government agency, or even a known contact to manipulate the victim into complying with a fraudulent request.',
    indicators: [
      'Message claims to be from a known brand or authority figure',
      'Creates urgency using the organization\'s name',
      'Requests are inconsistent with how the real organization communicates',
      'Sender number does not match official contact records',
    ],
    safeResponse:
      'Verify the identity of the sender through official channels independently. Do not use any contact information provided in the suspicious message.',
    prevention:
      'Familiarise yourself with how your bank and key services communicate. When in doubt, hang up and call back using the number on the official website.',
  },
  {
    key: 'attachments',
    title: 'Attachments and APKs',
    icon: '📎',
    definition:
      'Malware attacks trick users into downloading and installing malicious software disguised as documents, media files, or applications. APKs distributed outside the Play Store are a common delivery mechanism.',
    indicators: [
      'Request to download an APK file outside the Play Store or App Store',
      'Link to download a document from an unknown source',
      'Message claiming a file has been shared with you by a contact',
      'Request to install a remote access or screen-sharing application',
    ],
    safeResponse:
      'Do not download or install files from unknown sources. Only install applications from the official Google Play Store or Apple App Store.',
    prevention:
      'Disable "Install from unknown sources" on Android. Keep your device OS and apps updated. Verify with the supposed sender through a separate channel before opening any unexpected file.',
  },
];
