#!/usr/bin/env python

import gtk.glade
from time import gmtime, strftime
import datetime
from string import split

RATE_INCREMENT = 0.5
rate_list = [num * RATE_INCREMENT for num in range(1,11)]

def on_resetall_button_clicked(*args):
    print "Resetting..."
    for num in range(1,8):
        for entry in ['start_entry', 'finish_entry', 'diff_entry', 'total_entry']:
            xml.get_widget(entry + str(num)).delete_text(0,-1)
    
def on_start_button_clicked(*args):
    start_entry = xml.get_widget('start_entry' + args[0].name[-1])
    start_entry.set_text(strftime("%H:%M", gmtime()))

def on_finish_button_clicked(*args):
    button_num = args[0].name[-1]
    start_entry = xml.get_widget('start_entry' + button_num)
    finish_entry = xml.get_widget('finish_entry' + button_num)
    finish_time = strftime("%H:%M", gmtime())
    finish_entry.set_text(finish_time)
    
    sh, sm = split(start_entry.get_text(),':')
    start = datetime.datetime(2011,1,1,int(sh),int(sm),00)
    fh, fm = split(finish_time, ':')
    end = datetime.datetime(2011,1,1,int(fh),int(fm),00)

    delta = end - start
    print 'delta is %s' %str(delta)
    rate_widget = xml.get_widget('combobox' + button_num)
    rate = rate_list[rate_widget.props.active]
    diff_entry = xml.get_widget('diff_entry' + button_num)
    total_entry = xml.get_widget('total_entry' + button_num)
    diff_entry.set_text(str(delta))
    print 'rate used %s' %rate
    total_entry.set_text(str(total(delta.seconds, rate)))

def total(seconds, rate):
    minutes = seconds / 60
    hours = minutes / 60.0
    total = hours * rate
    total_rounded = round(total,2)
    return total_rounded 

def on_reset_button_clicked(*args):
    for entry in ['start_entry', 'finish_entry', 'diff_entry', 'total_entry']:
        xml.get_widget(entry + args[0].name[-1]).delete_text(0,-1)
    
if __name__ == '__main__':
    xml = gtk.glade.XML('spirale_time.glade')
    window = xml.get_widget('dialog1')
    window.connect("delete_event", gtk.main_quit)
    
    for i in range(1,8):
        xml.get_widget('combobox' + str (i)).set_active(3)
        xml.get_widget('start_button' + str(i)).connect("clicked", on_start_button_clicked)
        xml.get_widget('finish_button' + str(i)).connect("clicked", on_finish_button_clicked)
        xml.get_widget('reset_button' + str(i)).connect("clicked", on_reset_button_clicked)
        xml.get_widget('resetall').connect("clicked", on_resetall_button_clicked)
    
    window.show_all()
    gtk.main()
