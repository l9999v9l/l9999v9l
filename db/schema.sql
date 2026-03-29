-- SQL Schema for telemetry data

CREATE TABLE telemetry_raw (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    data JSONB
);

CREATE TABLE gpu_metrics (
    id SERIAL PRIMARY KEY,
    gpu_id INT NOT NULL,
    utilization FLOAT NOT NULL,
    memory_used INT NOT NULL,
    temperature INT NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE energy_audit (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    energy_consumed FLOAT NOT NULL,
    cost FLOAT NOT NULL
);

CREATE TABLE compute_audit (
    id SERIAL PRIMARY KEY,
    compute_time INT NOT NULL,
    job_id INT NOT NULL,
    success BOOLEAN NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

CREATE TABLE system_logs (
    id SERIAL PRIMARY KEY,
    log_message TEXT NOT NULL,
    log_level VARCHAR(10) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);