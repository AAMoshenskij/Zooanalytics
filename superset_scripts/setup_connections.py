#!/usr/bin/env python3

import requests
import json
import time

def setup_superset_connections():
    # URL Superset
    SUPERSET_URL = "http://localhost:8088"
    LOGIN_URL = f"{SUPERSET_URL}/api/v1/security/login"
    DATABASE_URL = f"{SUPERSET_URL}/api/v1/database/"
    
    # Данные для аутентификации
    login_payload = {
        "username": "admin",
        "password": "admin",
        "provider": "db",
        "refresh": True
    }
    
    # Заголовки
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    # Получение токена
    try:
        response = requests.post(LOGIN_URL, json=login_payload, headers=headers)
        response.raise_for_status()
        access_token = response.json()["access_token"]
        
        # Обновляем заголовки с токеном
        headers["Authorization"] = f"Bearer {access_token}"
        
        # Конфигурация для PostgreSQL
        postgres_config = {
            "database_name": "PetShop PostgreSQL",
            "sqlalchemy_uri": "postgresql://postgres:postgres@db:5432/abd2_db",
            "extra": json.dumps({
                "metadata_params": {},
                "engine_params": {"connect_args": {"sslmode": "prefer"}},
                "metadata_cache_timeout": {},
                "schemas_allowed_for_file_upload": []
            })
        }
        
        # Добавление PostgreSQL подключения
        response = requests.post(DATABASE_URL, json=postgres_config, headers=headers)
        if response.status_code in [200, 201]:
            print("✅ PostgreSQL connection added successfully")
        else:
            print(f"⚠️ PostgreSQL connection: {response.status_code} - {response.text}")
        
        # Конфигурация для ClickHouse
        clickhouse_config = {
            "database_name": "PetShop ClickHouse",
            "sqlalchemy_uri": "clickhouse://default:your_secure_password@clickhouse:8123/default",
            "extra": json.dumps({
                "metadata_params": {},
                "engine_params": {"connect_args": {"secure": False}},
                "metadata_cache_timeout": {},
                "schemas_allowed_for_file_upload": []
            })
        }
        
        # Добавление ClickHouse подключения
        response = requests.post(DATABASE_URL, json=clickhouse_config, headers=headers)
        if response.status_code in [200, 201]:
            print("✅ ClickHouse connection added successfully")
        else:
            print(f"⚠️ ClickHouse connection: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ Error setting up connections: {str(e)}")

if __name__ == "__main__":
    print("Waiting for Superset to be ready...")
    time.sleep(30)  # Даем Superset время на запуск
    setup_superset_connections()