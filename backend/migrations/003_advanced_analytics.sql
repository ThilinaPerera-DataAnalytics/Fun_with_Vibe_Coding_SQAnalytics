-- =====================================================
-- SQAnalytics Database Migration
-- Version: 1.1.0
-- Purpose: Advanced Analytics Foundation
-- Table: scan_events
-- =====================================================


-- Device Information

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS device_brand VARCHAR(100);


-- Geography Information

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS country VARCHAR(100);

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS country_code VARCHAR(10);

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS region VARCHAR(100);

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS city VARCHAR(100);

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS timezone VARCHAR(100);


-- Network Information

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS ip_hash VARCHAR(255);

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS language VARCHAR(50);


-- Session Information

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS session_id UUID;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS visitor_id UUID;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS first_visit BOOLEAN DEFAULT TRUE;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS returning_visitor BOOLEAN DEFAULT FALSE;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS visit_number INTEGER DEFAULT 1;


-- Redirect Information

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS destination_url TEXT;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS redirect_timestamp TIMESTAMP;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS redirect_success BOOLEAN DEFAULT FALSE;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS response_time_ms INTEGER;


-- Engagement Information

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS time_on_page INTEGER;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS bounce BOOLEAN;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS clicked_cta BOOLEAN DEFAULT FALSE;

ALTER TABLE scan_events
ADD COLUMN IF NOT EXISTS engagement_score INTEGER;


-- Verification

SELECT *
FROM scan_events
LIMIT 1;