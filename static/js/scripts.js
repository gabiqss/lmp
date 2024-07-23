
$(document).ready(function(){
    $('#id_cnpj').mask('00.000.000/0000-00', {reverse: true});
  
    $('#id_cnpj').blur(function(){
      var cnpj = $(this).val().replace(/[^0-9]/g, '');
  
      if(cnpj.length != 14){
        return false;
      }
  
      $.ajax({
        url: 'https://www.receitaws.com.br/v1/cnpj/' + cnpj,
        method: 'GET',
        dataType: 'jsonp',
        complete: function(xhr){
          var data = xhr.responseJSON;
  
          if(data.status === 'ERROR'){
            alert(data.message);
            return;
          }
  
          $('#id_name').val(data.nome);
          $('#id_email').val(data.email);
          $('#id_phone').val(data.telefone);
          $('#id_corporate_name').val(data.fantasia);
          $('#id_fax').val(data.fax);
          $('#id_web_site').val(data.site);
          $('#id_municipal_registration').val(data.municipio);
          $('#id_state_registration').val(data.uf);
          $('#id_address').val(data.logradouro);
          $('#id_city').val(data.municipio);
          $('#id_cep').val(data.cep);
          $('#id_address_number').val(data.numero);
          $('#id_neighborhood').val(data.bairro);
        }
      });
    });
  });
  
  