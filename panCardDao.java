package com.lti.dao;

import java.util.Optional;
import com.lti.dao.PanRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.lti.entity.panDetails;

@Component
public class panCardDao {

	@Autowired
	PanRepository Prepo;

	public boolean isPanCardPresent(String panId) {

		Optional<panDetails> optional = Prepo.findById(panId);
		return optional.isEmpty();

	}
		public String savedetails(panDetails pdetails) {
		try {
			Prepo.save(pdetails);

			return "true";
		} catch (Exception e) {
			return "false" + e;
		}
	}

}
