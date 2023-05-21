import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('sushi_cool.db')
    cur = base.cursor()
    if base:
        print('Data base connected ok!')
    else:
        print('Incorrect data')
    base.execute('create table if not exists menu(img text, name text primary key, description text, price text)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('insert into menu values (?,?,?,?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('select name, description, price from menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],\
        f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_read2():
    return cur.execute('select name, description, price from menu').fetchall()

async def sql_delete_command(data):
    cur.execute('delete from menu where name == ?', (data))
    base.commit()
