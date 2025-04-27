# Đây là file sql tham khảo
# Active: 1744842354217@@127.0.0.1@3307@

CREATE DATABASE personal_expense_management
    DEFAULT CHARACTER SET = 'utf8mb4';

USE personal_expense_management;

CREATE TABLE danh_muc (
    ma_danh_muc CHAR(36) PRIMARY KEY DEFAULT(UUID()),
    ma_tai_khoan CHAR(36),
    ten_danh_muc VARCHAR(255),
    phan_tram_phan_bo DECIMAL(4, 2),
    loai_danh_muc ENUM('Thu nhập', 'Chi Tiêu', 'Tiết kiệm', 'Đầu tư'),
    mo_ta TEXT
);

CREATE TABLE giao_dich (
    ma_giao_dich CHAR(36) PRIMARY KEY DEFAULT(UUID()),
    ma_danh_muc CHAR(36),
    ma_tai_khoan CHAR(36),
    ten_giao_dich VARCHAR(255),
    mo_ta TEXT,
    so_tien DECIMAL(10, 2),
    ngay_giao_dich DATE
);

CREATE TABLE tai_khoan(
    ma_tai_khoan CHAR(36) PRIMARY KEY DEFAULT(UUID()),
    ten_tai_khoan VARCHAR(255) UNIQUE,
    mat_khau VARCHAR(255)
);

ALTER TABLE giao_dich
    ADD CONSTRAINT fk_gd_tk_matk FOREIGN KEY (ma_tai_khoan) REFERENCES tai_khoan(ma_tai_khoan) ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT fk_gd_dm_madm FOREIGN KEY (ma_danh_muc) REFERENCES danh_muc(ma_danh_muc) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE danh_muc
    ADD CONSTRAINT fk_dm_tk_matk FOREIGN KEY (ma_tai_khoan) REFERENCES tai_khoan(ma_tai_khoan) ON DELETE CASCADE ON UPDATE CASCADE;
