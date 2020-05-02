from flask import Flask
import game
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    players = {'Denis':None,
                'DimaM':None,
                'TanyaP':None,
                'Danya':None,
                'NastyaSh':None,
                'TanyaR':None,
                'Sveta':None,
                'Ali':None,
                'Alice':None,
                'EgorM':None}
    roles_quantity, players = game.generate_roles_list(players)
    msg = []
    msg.append(str(datetime.datetime.today().hour))
    msg.append(':')
    msg.append(str(datetime.datetime.today().minute))
    msg.append('<br>')

    for i in roles_quantity:
        msg.append(i)
        msg.append(str(roles_quantity[i]))
        msg.append(':')

    msg.append('<br><br>')
    for p in players:
        msg.append('<b>')
        msg.append(p)
        msg.append('</b>')
        msg.append('-->')
        msg.append(players[p])
        msg.append('<br>')
        # print(p,'-->',players[p])
    msg = ' '.join(msg)
    return msg

if __name__ == '__main__':
    app.run(debug=True)




