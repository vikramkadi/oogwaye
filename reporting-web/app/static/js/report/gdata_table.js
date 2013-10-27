/*
 *  gdata_table.js:
 *  Wrapper API to google dataTable and fusionTable.
 */

    function fusionTableColumns( tableId, apiKey ) {
      // Construct query
      var url = "https://www.googleapis.com/fusiontables/v1/tables/" + tableId;
      url += "?key=" + apiKey;
      return url;
    }

    function fusionTableData( tableId, apiKey ) {
      // Construct query
      var query = "SELECT * FROM " + tableId;
      // Construct the URL
      var url = [ "https://www.googleapis.com/fusiontables/v1/query" ];
      url.push( "?sql=" + encodeURIComponent( query ) );
      url.push( "&key=" + apiKey );
      //url.push( "&typed=true" );
      return url.join( "" );
    }

    /*
    function newDataTable(sql_data) {
      var dataTable = new google.visualization.DataTable();
      for (var i = 0; i < sql_data.facts.length; i++) {
        var col = sql_data.facts[i];
        if (i==1 || i==2) {
          col.coltype = "string";
        } else {
          col.coltype = "number";
        }
        dataTable.addColumn( col.coltype, col.colname );
      }
      for (var i = 0; i < sql_data.dimensions.length; i++) {
        var col = sql_data.dimensions[i];
        dataTable.addColumn( col.coltype, col.colname );
      }
      dataTable.addRows(sql_data.data);
      return dataTable;
    }
    */
    
    function newDataTable( json ) {
      var dataTable = new google.visualization.DataTable();
      for (var i = 0; i < json.columns.length; i++) {
        var dataObject = json.columns[i];
        var dataType   = dataObject.type.toLowerCase();
        switch ( dataType ) {
          case "boolean":
          case "date":
          case "datetime":
          case "number":
          case "string":
          case "timeofday":
            break;
          case "location":
          default:
            dataType = "string";
            break;
        }
        dataTable.addColumn( dataType, dataObject.name, i );
      }
      return dataTable;
    }

    function loadDataTable( dataTable, json ) {
      $( json.rows ).each( function() {
      //for ( var i = 0; i < json.rows.length; i++ ) {
        //var row = json.rows[i];
        var typecastRow = $( this ).map( function( index, sval ) {
          switch ( dataTable.getColumnType( index ) ) {
            case "boolean":
              return parseInt( sval );
              break;
            case "number":
              return parseFloat( sval );
              break;            
            case "date":
            case "datetime":
            case "timeofday":
              return new Date( sval );
              break;
            default:
              return sval;
              break;
          }
        }).get();
        dataTable.addRow( typecastRow );
      });
      //}
      //dataTable.addRows( json.rows );
      return dataTable;
      //$( "#workbook" ).prop( "dataTable", newDataTable( json ) );
      //console.log( getDataTable() );
    }

    // Given array of column names, find corresponding indeces into dataTable
    function getDataTableColumnIndeces( colNames, dataTable ) {
      var colIndeces = $( colNames ).map( function() {
        for ( var i = 0; i < dataTable.H.length; i++ ) {
          if ( this == dataTable.H[i].label ) return i;
        }
        return; // Name not found, return nothing
      }).get();
      return colIndeces;
    }
