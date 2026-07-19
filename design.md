---
name: Clinical Intelligence System
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0058be'
  on-secondary: '#ffffff'
  secondary-container: '#2170e4'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#0b1c30'
  on-tertiary-container: '#75859d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#d3e4fe'
  tertiary-fixed-dim: '#b7c8e1'
  on-tertiary-fixed: '#0b1c30'
  on-tertiary-fixed-variant: '#38485d'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  container-padding: 24px
  gutter: 24px
---

## Brand & Style

The design system is engineered for the intersection of high-stakes healthcare and advanced artificial intelligence. It balances the sterile precision of clinical software with the sophisticated, fluid motion found in modern fintech interfaces. The personality is defined by "Clinical Trust"—a visual language that prioritizes legibility, data integrity, and a calm user experience to reduce cognitive load in medical environments.

The aesthetic draws from **Minimalism** and **Corporate Modern** movements, utilizing a "Structured Air" approach: large whitespace, thin 1px functional borders, and subtle depth layers. It mirrors the premium feel of high-end consumer health hardware, ensuring the AI components feel like a supportive tool rather than a disruptive technology.

## Colors

The palette is anchored by **Deep Navy (#0F172A)**, used for high-contrast typography and authoritative structural elements. **Medical Blue (#3B82F6)** serves as the primary action and intelligence indicator, representing the "AI layer." 

**Slate Gray (#64748B)** is utilized for secondary information and metadata to maintain visual hierarchy without clutter. Surfaces primarily use **Pure White (#FFFFFF)** for the base layer, with **Soft Blue (#F8FAFC)** defining container backgrounds and subtle sectioning. Semantic colors (Success, Warning, Error) must be desaturated to fit the clinical aesthetic while maintaining functional visibility.

## Typography

This design system exclusively utilizes **Inter** to leverage its exceptional legibility and systematic weight distribution. Headlines are "Confident," using semi-bold weights with negative letter spacing to create a dense, professional impact. 

Body text emphasizes readability with generous line heights (1.6x) and slight tracking increases for long-form medical reports. Labels and metadata use a slightly heavier weight and increased tracking to remain distinct from body prose at smaller sizes.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** approach for desktop dashboards to ensure data consistency, transitioning to a **Fluid Grid** for tablet and mobile devices. 

- **Desktop (1440px+):** 12-column grid, 1200px max-width, 24px gutters.
- **Tablet (768px - 1439px):** 8-column grid, fluid width, 24px margins.
- **Mobile (<767px):** 4-column grid, fluid width, 16px margins.

Spacing follows a strict 8px linear scale. Section containers should utilize `spacing-xl` (48px) to create the "large whitespace" characteristic of the brand style, while internal component spacing remains tight (`spacing-sm`) for a compact, clinical feel.

## Elevation & Depth

Visual hierarchy is established through **Tonal Layers** and **Soft Ambient Shadows**. 

1.  **Base Layer:** Pure White (#FFFFFF) for the primary application background.
2.  **Surface Layer:** Soft Blue (#F8FAFC) used for recessed backgrounds or subtle card containers.
3.  **Elevated Layer:** White cards with a 1px border (#E2E8F0) and a very soft, diffused shadow (0px 4px 20px rgba(15, 23, 42, 0.05)).
4.  **Floating Layer:** Used for modals and tooltips, utilizing a more pronounced shadow (0px 10px 30px rgba(15, 23, 42, 0.10)).

Avoid heavy drop shadows. Depth should feel like stacked sheets of high-quality paper rather than floating objects.

## Shapes

The shape language is defined by modern, generous curves that soften the clinical nature of the product. 

- **Primary Containers:** 16px to 24px corner radius (Rounded-XL) to create distinct, approachable "buckets" of information.
- **Components:** Buttons and input fields use an 8px radius (Rounded-MD).
- **Interactive Small Elements:** Chips and badges use a Pill-shaped (fully rounded) radius to distinguish them from structural elements.

## Components

### Buttons & Inputs
- **Primary Action:** Solid Deep Navy or Medical Blue with white text. High-contrast, 8px radius.
- **Secondary Action:** Ghost style with a 1px border (#E2E8F0) and Deep Navy text.
- **Input Fields:** White background with a 1px Slate Gray border that transitions to Medical Blue on focus.

### Status & Intelligence
- **Confidence Badges:** Used for AI-generated data. Features a Soft Blue background with Medical Blue text and a percentage indicator.
- **Status Pills:** High-contrast backgrounds for critical states (e.g., Red for "Urgent") and subtle, low-opacity backgrounds for standard states.
- **Expandable Cards:** Base 24px rounded containers. Use a "Chevron" icon for state changes. Headers should use `headline-sm` with 24px internal padding.

### Lists & Navigation
- **Medical Lists:** Clean rows separated by 1px horizontal lines (#F1F5F9). Left-aligned icons in Slate Gray.
- **Sidebar:** Minimalist, using Deep Navy for the active state and Slate Gray for inactive icons/labels.