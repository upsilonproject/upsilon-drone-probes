#!groovy                                                                           

properties(                                                                        
    [                                                                              
        [                                                                          
            $class: 'jenkins.model.BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '10', artifactNumToKeepStr: '10'],
            $class: 'CopyArtifactPermissionProperty', projectNames: '*'            
        ]                                                                          
    ]                                                                              
)                                                                                  

def buildRpm(dist) {                                                               
    deleteDir()                                                                    

	prepareEnv()
                                                                                                                                                                      
    sh 'unzip -jo SOURCES/upsilon-serviceChecks-*.zip "upsilon-serviceChecks-*/var/pkg/upsilon-serviceChecks.spec" "upsilon-serviceChecks-*/.buildid.rpmmacro" -d SPECS/'
    sh "find ${env.WORKSPACE}"                                                     
                                                                                   
    sh "rpmbuild -ba SPECS/upsilon-serviceChecks.spec --define '_topdir ${env.WORKSPACE}' --define 'dist ${dist}'"
                                                                                   
    archive 'RPMS/noarch/*.rpm'                                                    
}                    

node {
	stage "Build"

	deleteDir()
	checkout scm

	sh './make.sh'

	stash includes: '*.zip', name: 'binaries'
}

stage "Package"

node {                                                                             
    buildRpm("el7")                                                                
}                                                                                  
                                                                                   
node {                                                                             
    buildRpm("el6")                                                                
}                                                                                  
                                                                                   
node {                                                                             
    buildRpm("fc24")                                                               
}


