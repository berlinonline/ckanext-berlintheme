import difflib

class GridDiff(object):

    def __init__(self):
        self._prefix = ["from_","to_"]

    def _collect_lines(self,diffs):
        """Collects mdiff output into separate lists

        Before storing the mdiff from/to data into a list, it is converted
        into a single line of text with HTML markup.
        """

        fromlist,tolist,flaglist = [],[],[]
        # pull from/to data and flags from mdiff style iterator
        for fromdata, todata, flag in diffs:
            try:
                # store HTML markup of the lines into the lists
                fromlist.append(self._format_line(0,flag,*fromdata))
                tolist.append(self._format_line(1,flag,*todata))
            except TypeError:
                # exceptions occur for lines where context separators go
                fromlist.append(None)
                tolist.append(None)
            flaglist.append(flag)
        return fromlist,tolist,flaglist

    def _format_line(self,side,flag,linenum,text):
        """Returns HTML markup of "from" / "to" text lines

        side -- 0 or 1 indicating "from" or "to" text
        flag -- indicates if difference on line
        linenum -- line number (used for line number column)
        text -- line text to be marked up
        """
        try:
            linenum = '%d' % linenum
            id = ' id="%s%s"' % (self._prefix[side],linenum)
        except TypeError:
            # handle blank lines where linenum is '>' or ''
            id = ''
        # replace those things that would get confused with HTML symbols
        text=text.replace("&","&amp;").replace(">","&gt;").replace("<","&lt;")

        return '''
        <div class="diff_subcell diff_index"%s>%s</div>
        <div class="diff_subcell diff_content">%s</div>
        ''' % (id, linenum, text)

    def make_grid(self, fromlines: list, tolines: list):

        diffs = difflib._mdiff(fromlines, tolines)

        fromlist, tolist, flaglist = self._collect_lines(diffs)

        # fromlist, tolist, flaglist, next_href, next_id = self._convert_flags(fromlist,tolist,flaglist)

        rows = []
        row_template = '''
        <div class="diff_cell diff_current">
            <div class="diff_subcell diff_next"></div>
            %s
        </div>
        <div class="diff_cell diff_incoming">
            <div class="diff_subcell diff_next"></div>
            %s
        </div>
        '''

        for i in range(len(flaglist)):
            rows.append( row_template % (fromlist[i], tolist[i]))
        
        rows = "\n".join(rows)

        grid = f'<div class="diffs">{rows}</div>'

        return grid.replace('\0+','<span class="diff_add">'). \
                    replace('\0-','<span class="diff_sub">'). \
                    replace('\0^','<span class="diff_chg">'). \
                    replace('\1','</span>'). \
                    replace('\t','&nbsp;')

