## API

<strong>/getTicketDatas/artistName</strong>

- `GET` : 해당 가수 티켓 정보 가져와서 티켓 정보에 저장

<br>

<strong>/api/tickets</strong>

- `GET` : 모든 티켓 정보 조회

    <strong>Response</strong>

    ```
    [
        {
            "id": 79,
            "artist_id": 22,
            "artist": "그랜드 민트 페스티벌",
            "title": "그랜드 민트 페스티벌 2022 at 올림픽공원 88잔디마당 / 88호수 수변무대 (2022-10-22 ~ 2022-10-23)",
            "date": "2022.08.23",
            "date_full": "2022.08.23(화) 오후 6:00",
            "link": "https://t.co/yedw22zacH",
            "performance_info": "그랜드 민트 페스티벌-2022.08.23(화) 오후 6:00"
        },
        ...
    ]
    ```

<br>

<strong>/api/ticket</strong>

- `POST`: 티켓 추가

<br>

<strong>api/ticket/id</strong>

- `GET`: 티켓 조회

    <strong>Response</strong>

    ```
    {
        "id": 81,
        "artist_id": 24,
        "artist": "다린",
        "title": "2022 다린 콘서트 Orb: at 노들섬 라이브하우스 (2022-10-29 ~ 2022-10-30)",
        "date": "2022.09.05",
        "date_full": "2022.09.05(월) 오후 8:00",
        "link": "https://t.co/QL2bJykpcd",
        "performance_info": "다린-2022.09.05(월) 오후 8:00"
    }
    ```
- `PATCH`: 티켓 수정
- `DELETE`: 티켓 삭제

<br>

<strong>api/artists</strong>

- `GET` : 모든 티켓 정보 조회

    <strong>Response</strong>

    ```
    [
        {
            "id": 22,
            "name": "그랜드 민트 페스티벌",
            "artist": [
                {
                    "id": 79,
                    "artist_id": 22,
                    "artist": "그랜드 민트 페스티벌",
                    "title": "그랜드 민트 페스티벌 2022 at 올림픽공원 88잔디마당 / 88호수 수변무대 (2022-10-22 ~ 2022-10-23)",
                    "date": "2022.08.23",
                    "date_full": "2022.08.23(화) 오후 6:00",
                    "link": "https://t.co/yedw22zacH",
                    "performance_info": "그랜드 민트 페스티벌-2022.08.23(화) 오후 6:00"
                },
                ...
            ],
            "color": "#38ffbd"
        },
        ...
    ]
    ```
<br>

<strong>api/artist</strong>

- `POST` : 가수 추가

<br>

<strong>api/artist/id</strong>

- `GET`: 가수 조회

    <strong>Response</strong>

    ```
    {
        "id": 26,
        "name": "SURL",
        "artist": [
            {
                "id": 86,
                "artist_id": 26,
                "artist": "SURL",
                "title": "MPMG WEEK 2023： MPMG MUSIC LIVE - SURL(설), 솔루션스, 쏜애플",
                "date": "2023.01.17",
                "date_full": "2023.01.17(화) 18:00",
                "link": "https://t.co/d6ZfhHCfhS",
                "performance_info": "SURL-2023.01.17(화) 18:00"
            },
            ...
        ],
        "color": "#ff9ec0"
    }
    ```
- `PATCH`: 가수 수정
- `DELETE`: 가수 삭제

## 추가 하고 싶은 사항
- [ ] yes24티켓 말고 다른 예매사 정보도 받아오기
- [ ] 중복된 공연 정보 처리
