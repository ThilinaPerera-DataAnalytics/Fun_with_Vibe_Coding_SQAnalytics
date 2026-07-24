-- =====================================================
-- SQAnalytics Database Migration
-- Version: 1.2.0
-- Purpose: Human Friendly QR URLs
-- =====================================================

ALTER TABLE qr_codes
ADD COLUMN IF NOT EXISTS display_slug VARCHAR(255);