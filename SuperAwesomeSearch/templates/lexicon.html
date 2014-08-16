<%inherit file="layout.html"/>

<%block name="title">Field terms</%block>

<form name="form" id="form" method="get">
    <select name="fieldname" id="fieldname" onchange="$('form').submit()">
            % for fname in reader.schema.names():
                <option value="${fname}" ${'selected' if fname == fieldname else ''}>
                ${fname}
                </option>
            % endfor
    </select>
    <input type="submit">
</form>

<p>Field: ${ fieldname }</p>

<div id="results">
        % if fieldname:
        <table class="table-striped table-condensed">
            <tr>
                <th>Text</th>
                <th>Doc freq</th>
                <th>Weight</th>
                <th>Min len</th>
                <th>Max len</th>
                <th>Max weight</th>
                <th>Min docnum</th>
                <th>Max docnum</th>
            </tr>

        % for text, tinfo in reader.iter_field(fieldname):
                <tr>
                    <td>
                        <a href="/?q=${fieldname}:${text.encode("string-escape") | u}">
                            <tt>${ text.encode("string-escape") }</tt>
                        </a>
                    </td>
                    <td>${tinfo.doc_frequency()}</td>
                    <td>${tinfo.weight()}</td>
                    <td>${tinfo.min_length()}</td>
                    <td>${tinfo.max_length()}</td>
                    <td>${tinfo.max_weight()}</td>
                    <td>${tinfo.min_id()}</td>
                    <td>${tinfo.max_id()}</td>
                </tr>
        % endfor
        </table>
        % else:
            No input
        % endif
</div>
