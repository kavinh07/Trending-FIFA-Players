from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def get_national_team(national_team):
    national_team_list = []
    for idx, row in enumerate(national_team):
        if (idx-1)%3 == 0:
            national_team_list.append(str(row.get_attribute("title")))
        
    return national_team_list

def get_name_club_contract(names_club_contracts):
    name = []
    club = []
    contract = []
    for idx, row in enumerate(names_club_contracts):
        if idx%2 != 0:
            s = str(row.text)
            n = s.split("\n")
            club.append(n[0])
            contract.append(n[1])

        else:
            name.append(row.text)
    return name, club, contract
def get_all_stats(states):
    l = []
    age = []
    ovl = []
    povl = []
    val = []
    wag = []
    tst = []
    for idx, row in enumerate(states):
        index = idx+1
        if index%6 == 0:
            l.append(row.text)
            age.append(l[0])
            ovl.append(l[1])
            povl.append(l[2])
            val.append(l[3])
            wag.append(l[4])
            tst.append(l[5])
            l.clear()
            
        else:
            l.append(row.text)
    return age, ovl, povl, val, wag, tst

def get_player_image(player_img):
    images = []
    for idx, row in enumerate(player_img):
        images.append(row.get_attribute("src"))
    return images

def get_player_positions(player_pos):
    pos_list = []
    for idx, rows in enumerate(player_pos):
        if idx%2 == 0:
            pos = rows.find_elements(By.CLASS_NAME, "pos")
            poss = []
            for row in pos:
                poss.append(row.text)
            pos_list.append(poss)

    return pos_list

def get_dataframe(pl_names, pl_image, age, national_team, position, overall, p_overall, team, contract, value, wage, t_state):
    df = pd.DataFrame({"Player_name": pl_names,
                        "Images": pl_image,
                        "Age": age,
                        "National_team": national_team,
                        "Positions": position,
                        "Overall": overall,
                        "Potential_overall": p_overall,
                        "Current_club": team,
                        "Current_contract": contract,
                        "Value": value,
                        "Wage": wage, 
                        "Total_stats": t_state
                        })
    return df

def get_appender(main_list, sublist):
    for elements in sublist:
        main_list.append(elements)
    
    return main_list

def main():
    url = "https://sofifa.com/players"
    driver = webdriver.Edge()
    driver.get(url)
    print("Entered the weblink")
    NAME = []
    IMAGE = []
    AGE = []
    NATIONAL_TEAM = []
    POSITION = []
    OVERALL = []
    P_OVERALL = []
    TEAM = []
    CONTRACT = []
    VALUE = []
    WAGE = []
    T_STATS = []
    num_webpages = 50
    for i in range(num_webpages):
        #Scrolling to the end
        page_height = driver.execute_script("return document.body.scrollHeight")
        for i in range(int(page_height/200)):
            driver.execute_script("window.scrollBy(0,200);")
            time.sleep(2)
        
        #Collecting data
        players = driver.find_element(By.CLASS_NAME, "list")
        names_club_contracts = players.find_elements(By.CLASS_NAME, "ellipsis")
        national_team = players.find_elements(By.TAG_NAME, "img")
        states = players.find_elements(By.CLASS_NAME, "col")
        player_img = players.find_elements(By.CLASS_NAME, "player-check")
        player_pos = players.find_elements(By.CLASS_NAME, "col-name")

        #List collecttion 
        names, clubs, contracts = get_name_club_contract(names_club_contracts)
        national_teams = get_national_team(national_team)
        ages, ovls, povls, vals, wags, tsts = get_all_stats(states)
        pl_imgs = get_player_image(player_img)
        pl_poss = get_player_positions(player_pos)
        NAME = get_appender(NAME, names)
        TEAM = get_appender(TEAM, clubs)
        CONTRACT = get_appender(CONTRACT, contracts)
        NATIONAL_TEAM = get_appender(NATIONAL_TEAM, national_teams)
        AGE = get_appender(AGE, ages)
        OVERALL = get_appender(OVERALL, ovls)
        P_OVERALL = get_appender(P_OVERALL, povls)
        VALUE = get_appender(VALUE, vals)
        WAGE = get_appender(WAGE, wags)
        T_STATS = get_appender(T_STATS, tsts)
        IMAGE = get_appender(IMAGE, pl_imgs)
        POSITION = get_appender(POSITION, pl_poss)
        print("Its all good")

        #Going to next page
        pagination = driver.find_element(By.CLASS_NAME, "pagination")
        next_btn = pagination.find_elements(By.CLASS_NAME, 'bp3-button-text')
        for buttons in next_btn:
            if str(buttons.text) == "NEXT":
                buttons.click()
                break
    driver.quit()
    dataframe = get_dataframe(NAME, IMAGE, AGE, NATIONAL_TEAM, POSITION, OVERALL, P_OVERALL, TEAM, CONTRACT, VALUE, WAGE, T_STATS)
    dataframe.to_excel("data\\trending_football_players.xlsx", index= False)
    return


if __name__ == "__main__":
    main()