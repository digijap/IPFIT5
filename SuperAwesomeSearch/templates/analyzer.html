<%inherit file="layout.html"/>

<%block name="title">Analyzers</%block>

<form name="form" id="form" method="get">
    <input name="q" id="q" value="${ q }">
    <select name="fieldname" id="fieldname" onchange="$('form').submit()">
        % for fname, field in searcher.schema.items():
            % if hasattr(field, "analyzer") and field.analyzer:
                <option value="${fname}" ${'selected' if fname == fieldname else ''}>
                ${fname}: ${repr(field.analyzer)}
                </option>
            % endif
        % endfor
    </select>
    <input type="submit">
</form>

<p>Field: ${ fieldname }</p>

<div id="results">
% if fieldname and q:
    <table class="table">
        <tr>
            <th>Pos</th>
            <th>Text</th>
            <th>Start char</th>
            <th>End char</th>
        </tr>

    % for i, token in enumerate(searcher.schema[fieldname].tokenize(q, positions=True, chars=True)):
        <tr>
            <td>${token.pos}</td>
            <td><tt>${token.text}</tt></td>
            <td>${token.startchar}</td>
            <td>${token.endchar}</td>
        </tr>
    % endfor
    </table>
% else:
    No input
% endif
</div>

