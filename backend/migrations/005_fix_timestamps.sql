-- =====================================================
-- Migration 005
-- Automatically manage timestamps
-- =====================================================

ALTER TABLE qr_codes
ALTER COLUMN created_at
SET DEFAULT NOW();

ALTER TABLE qr_codes
ALTER COLUMN updated_at
SET DEFAULT NOW();