import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

STOCK_FILE = 'stock.xlsx'

def load_stocks():
    """주식 데이터를 Excel 파일에서 불러옵니다."""
    try:
        df = pd.read_excel(STOCK_FILE)
        # 데이터 로드 시 종목코드를 문자열로 유지
        df['종목코드'] = df['종목코드'].astype(str)
    except FileNotFoundError:
        # 파일이 없으면 빈 DataFrame 생성
        return pd.DataFrame(columns=['종목코드', '종목명', '현재가', '시가총액', 'PER'])
    return df

def save_stocks(df):
    """주식 데이터를 Excel 파일에 저장합니다."""
    # 데이터를 저장할 때도 종목코드를 문자열로 유지
    df['종목코드'] = df['종목코드'].astype(str)
    df.to_excel(STOCK_FILE, index=False)

@app.route('/')
def index():
    """메인 페이지 - 주식 목록을 보여주고, 검색, 정렬, 페이지네이션을 지원합니다."""
    stocks_df = load_stocks()

    # 검색
    search_query = request.args.get('search', '')
    if search_query:
        # 종목명 또는 종목코드로 검색 (대소문자 구분 없이)
        stocks_df = stocks_df[
            stocks_df['종목명'].str.contains(search_query, case=False, na=False) |
            stocks_df['종목코드'].str.contains(search_query, case=False, na=False)
        ]

    # 정렬
    sort_by = request.args.get('sort_by', '종목명')
    order = request.args.get('order', 'asc')
    if sort_by in stocks_df.columns:
        is_ascending = order == 'asc'
        # 숫자형 데이터와 문자형 데이터를 구분하여 정렬
        if pd.api.types.is_numeric_dtype(stocks_df[sort_by]):
            stocks_df = stocks_df.sort_values(by=sort_by, ascending=is_ascending)
        else:
            stocks_df = stocks_df.sort_values(by=sort_by, ascending=is_ascending, key=lambda col: col.str.lower())


    # 페이지네이션
    page = request.args.get('page', 1, type=int)
    PER_PAGE = 8
    total_items = len(stocks_df)
    total_pages = (total_items + PER_PAGE - 1) // PER_PAGE
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    paginated_stocks_df = stocks_df.iloc[start:end]

    stocks = paginated_stocks_df.to_dict('records')

    return render_template(
        'index.html',
        stocks=stocks,
        page=page,
        total_pages=total_pages,
        sort_by=sort_by,
        order=order,
        search_query=search_query
    )

@app.route('/add', methods=['GET', 'POST'])
def add_stock():
    """새 주식 정보를 추가합니다."""
    if request.method == 'POST':
        new_stock = {
            '종목코드': request.form['code'],
            '종목명': request.form['name'],
            '현재가': int(request.form['price']),
            '시가총액': request.form['market_cap'],
            'PER': float(request.form['per'])
        }
        
        stocks_df = load_stocks()
        new_df = pd.DataFrame([new_stock])
        stocks_df = pd.concat([stocks_df, new_df], ignore_index=True)
        
        save_stocks(stocks_df)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:row_id>', methods=['GET', 'POST'])
def edit_stock(row_id):
    """기존 주식 정보를 수정합니다."""
    stocks_df = load_stocks()
    stock_to_edit = stocks_df.iloc[row_id].to_dict()

    if request.method == 'POST':
        # 폼에서 받은 데이터로 DataFrame을 업데이트합니다.
        stocks_df.loc[row_id, '종목코드'] = request.form['code']
        stocks_df.loc[row_id, '종목명'] = request.form['name']
        stocks_df.loc[row_id, '현재가'] = int(request.form['price'])
        stocks_df.loc[row_id, '시가총액'] = request.form['market_cap']
        stocks_df.loc[row_id, 'PER'] = float(request.form['per'])
        
        save_stocks(stocks_df)
        return redirect(url_for('index'))

    return render_template('edit.html', stock=stock_to_edit, row_id=row_id)

@app.route('/delete/<int:row_id>')
def delete_stock(row_id):
    """주식 정보를 삭제합니다."""
    stocks_df = load_stocks()
    stocks_df = stocks_df.drop(stocks_df.index[row_id]).reset_index(drop=True)
    save_stocks(stocks_df)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)